import P42CapabilityObligationGeometry

/- EvoNOMOS P42-P2-R6. Tiny explicit historical interface-signature incidence
   model: Go compiler executions are independent empirical witnesses.
   No universal source-to-Lean compiler simulation or new fundamental TCS law.
   The two upstream changes were merged in two INDEPENDENT projects in 2024.
-/
namespace P42R6

inductive Revision where
  | before
  | after
  deriving Repr, DecidableEq

inductive Boundary where
  | chiWrap
  | grpcPool
  | grpcCodecOld
  | grpcCodecV2
  deriving Repr, DecidableEq

inductive Signature where
  | stableWriterMethods
  | discard
  | getByteSlice
  | putByteSlice
  | getPointer
  | putPointer
  | codecLegacy
  | codecV2
  deriving Repr, DecidableEq

inductive Provider where
  | chiLegacy
  | chiRepaired
  | poolLegacy
  | poolPointer
  | codecLegacy
  | codecV2
  deriving Repr, DecidableEq

def boundaryExists (r : Revision) (b : Boundary) : Bool :=
  !(r == .before && b == .grpcCodecV2)

def requires (r : Revision) (b : Boundary) (s : Signature) : Bool :=
  match b with
  | .chiWrap =>
      (s == .stableWriterMethods) || (r == .after && s == .discard)
  | .grpcPool =>
      if r == .before then
        (s == .getByteSlice) || (s == .putByteSlice)
      else (s == .getPointer) || (s == .putPointer)
  | .grpcCodecOld => s == .codecLegacy
  | .grpcCodecV2 => s == .codecV2

def provides (p : Provider) (s : Signature) : Bool :=
  match p with
  | .chiLegacy => s == .stableWriterMethods
  | .chiRepaired => s == .stableWriterMethods || s == .discard
  | .poolLegacy => s == .getByteSlice || s == .putByteSlice
  | .poolPointer => s == .getPointer || s == .putPointer
  | .codecLegacy => s == .codecLegacy
  | .codecV2 => s == .codecV2

def signatureSatisfied (r : Revision) (b : Boundary)
    (p : Provider) : Bool :=
  boundaryExists r b &&
  (!(requires r b .stableWriterMethods) || provides p .stableWriterMethods) &&
  (!(requires r b .discard) || provides p .discard) &&
  (!(requires r b .getByteSlice) || provides p .getByteSlice) &&
  (!(requires r b .putByteSlice) || provides p .putByteSlice) &&
  (!(requires r b .getPointer) || provides p .getPointer) &&
  (!(requires r b .putPointer) || provides p .putPointer) &&
  (!(requires r b .codecLegacy) || provides p .codecLegacy) &&
  (!(requires r b .codecV2) || provides p .codecV2)

theorem historical_chi_addition_cuts_external_provider :
    signatureSatisfied .before .chiWrap .chiLegacy = true ∧
    signatureSatisfied .after .chiWrap .chiLegacy = false ∧
    signatureSatisfied .before .chiWrap .chiRepaired = true ∧
    signatureSatisfied .after .chiWrap .chiRepaired = true := by decide

theorem historical_grpc_signature_substitution :
    signatureSatisfied .before .grpcPool .poolLegacy = true ∧
    signatureSatisfied .after .grpcPool .poolLegacy = false ∧
    signatureSatisfied .before .grpcPool .poolPointer = false ∧
    signatureSatisfied .after .grpcPool .poolPointer = true := by decide

theorem historical_grpc_parallel_boundary_retains_old_contract :
    signatureSatisfied .before .grpcCodecOld .codecLegacy = true ∧
    signatureSatisfied .after .grpcCodecOld .codecLegacy = true ∧
    signatureSatisfied .before .grpcCodecV2 .codecV2 = false ∧
    signatureSatisfied .after .grpcCodecV2 .codecV2 = true := by decide

/- At this interface boundary the two methods are present by NAME in both
   versions; conformance nevertheless reverses because their TYPE SIGNATURES
   differ. Numeric interface cardinality is not a conformance statistic. -/
def poolMethodCount (_ : Revision) : Nat := 2
theorem equal_method_count_with_opposite_external_conformance :
    poolMethodCount .before = poolMethodCount .after ∧
    signatureSatisfied .before .grpcPool .poolLegacy ≠
      signatureSatisfied .after .grpcPool .poolLegacy := by decide

/- A deliberate restricted source-edit grammar: exactly two independent
   method-signature declarations of a fixed old provider may be replaced.
   Not a universal cheapest repair among wrappers, adapters and refactors. -/
def poolSignatureRepair (fixGet fixPut : Bool) : Bool :=
  fixGet && fixPut

theorem both_method_sites_necessary_for_this_repair_grammar
    (getRepaired putRepaired : Bool)
    (h : poolSignatureRepair getRepaired putRepaired = true) :
    getRepaired = true ∧ putRepaired = true := by
  cases getRepaired <;> cases putRepaired <;> simp_all [poolSignatureRepair]

theorem one_method_repair_insufficient :
    poolSignatureRepair true false = false ∧
    poolSignatureRepair false true = false ∧
    poolSignatureRepair true true = true := by decide

/- Adds one method name to an existing interface, unlike introducing a new
   parallel opt-in interface that preserves the pre-existing contract.
   This is a classical method-set/constraint-incidence distinction. -/
theorem direct_extension_and_parallel_extension_are_distinct :
    signatureSatisfied .before .chiWrap .chiLegacy = true ∧
    signatureSatisfied .after .chiWrap .chiLegacy = false ∧
    signatureSatisfied .before .grpcCodecOld .codecLegacy = true ∧
    signatureSatisfied .after .grpcCodecOld .codecLegacy = true := by decide

/- No semantic correctness follows from merely satisfying a type signature:
   the empty/no-op Discard implementation can typecheck but not implement
   a client's required discard-to-tee effect. Caller contracts are separate. -/
def effectsConform (_p : Provider) : Bool := false
theorem nominal_signature_repair_does_not_establish_discard_effects :
    signatureSatisfied .after .chiWrap .chiRepaired = true ∧
    effectsConform .chiRepaired = false := by decide

end P42R6
