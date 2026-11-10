"""Restricted product theorem tests plus 20,736 exhaustive permission/cost instances."""
from fractions import Fraction as Q
from itertools import product
import unittest
from compositional_authority import Module,binary,risk,oracle,joint,risk_decomposition

class CompositionalAuthority(unittest.TestCase):
    def test_independent_exact_factorization(self):
        a=binary()
        b=binary(losses=((Q(0),Q(5)),(Q(2),Q(0))))
        global_result=joint(a,b)
        self.assertEqual(global_result["risk"],risk(a)+risk(b))
        self.assertEqual(global_result["oracle"],oracle(a)+oracle(b))
        self.assertEqual(global_result["regret"],Q(3,2))
    def test_shared_action_permission_breaks_product(self):
        a=binary(observations=("s0","s1"))
        b=binary(observations=("s0","s1"))
        self.assertEqual(joint(a,b)["risk"],0)
        tied=joint(a,b,shared_actions={("0","0"),("1","1")})
        self.assertEqual(tied["risk"],Q(1,2))
        self.assertEqual(tied["oracle"],Q(1,2))
    def test_missing_common_permission_cannot_be_fixed_by_same_information(self):
        a=binary(feasible=(frozenset({"0"}),frozenset({"1"})))
        b=binary()
        self.assertIsNone(risk(a))
        self.assertEqual(joint(a,b)["status"],"NO_UNIFORM_AUTHORIZED_ACTION")
        richer=binary(observations=("s0","s1"),feasible=a.feasible)
        self.assertIsNotNone(risk(richer))
    def test_correlated_remote_observation_invalidates_local_factorization(self):
        a=binary()
        b=binary(observations=("b0","b1"),losses=((Q(0),Q(0)),(Q(0),Q(0))))
        weights={(0,0):Q(1,2),(1,1):Q(1,2)}
        self.assertEqual(risk(a),Q(1,2))
        self.assertEqual(joint(a,b,joint_p=weights)["risk"],Q(0))
    def test_nonadditive_cross_cost_breaks_product(self):
        a=binary(observations=("a0","a1"))
        b=binary(observations=("b0","b1"))
        coupled={(i,j,str(i),str(j)):Q(3) for i,j in product(range(2),repeat=2)}
        self.assertEqual(joint(a,b,extra=coupled)["risk"],Q(1))
        self.assertEqual(risk(a)+risk(b),Q(0))
    def test_zero_constrained_regret_is_not_zero_actual_cost(self):
        a=binary(observations=("a0","a1"),feasible=(frozenset({"0"}),frozenset({"0"})))
        b=binary(observations=("b0","b1"))
        r=joint(a,b)
        self.assertEqual(r["regret"],Q(0))
        self.assertEqual(r["risk"],Q(1,2))
    def test_authority_and_information_deficits_are_not_synonyms(self):
        # Full state signal, but one source action is prohibited in a possible state.
        a=binary(observations=("a0","a1"),feasible=(frozenset({"0"}),frozenset({"0"})))
        b=binary(observations=("b0","b1"))
        d=risk_decomposition(a,b)
        self.assertEqual(d["authority_deficit"],Q(1,2))
        self.assertEqual(d["observation_deficit"],Q(0))
        # Authorized actions exist everywhere; only hidden signal prevents adaptation.
        hidden=binary()
        e=risk_decomposition(hidden,b)
        self.assertEqual(e["authority_deficit"],Q(0))
        self.assertEqual(e["observation_deficit"],Q(1,2))

    def test_shared_owner_rights_create_pure_authority_deficit(self):
        a=binary(observations=("a0","a1"))
        b=binary(observations=("b0","b1"))
        d=risk_decomposition(a,b,shared_actions={("0","0"),("1","1")})
        self.assertEqual(d["authority_deficit"],Q(1,2))
        self.assertEqual(d["observation_deficit"],Q(0))
        self.assertEqual(d["total_deficit"],Q(1,2))

    def test_no_safe_hidden_permission_policy_is_not_numeric_regret(self):
        a=binary(feasible=(frozenset({"0"}),frozenset({"1"})))
        b=binary()
        d=risk_decomposition(a,b)
        self.assertEqual(d["status"],"NO_CERTIFIED_UNIFORMLY_AUTHORIZED_POLICY")
        self.assertNotIn("observation_deficit",d)

    def test_exhaust_20736_action_right_and_binary_cost_tables(self):
        options=(frozenset({"0"}),frozenset({"1"}),frozenset({"0","1"}))
        trials=0
        for m in range(16):
            la=tuple(tuple(Q((m>>(2*i+j))&1) for j in range(2)) for i in range(2))
            for n in range(16):
                lb=tuple(tuple(Q((n>>(2*i+j))&1) for j in range(2)) for i in range(2))
                for rights_a in product(options,repeat=2):
                    a=binary(feasible=rights_a,losses=la)
                    for rights_b in product(options,repeat=2):
                        b=binary(feasible=rights_b,losses=lb)
                        result=joint(a,b)
                        ra,rb=risk(a),risk(b)
                        if ra is None or rb is None:
                            self.assertEqual(result["status"],"NO_UNIFORM_AUTHORIZED_ACTION")
                        else:
                            self.assertEqual(result["risk"],ra+rb)
                            self.assertEqual(result["oracle"],oracle(a)+oracle(b))
                        trials+=1
        self.assertEqual(trials,20736)

if __name__=="__main__":
    unittest.main(verbosity=2)
