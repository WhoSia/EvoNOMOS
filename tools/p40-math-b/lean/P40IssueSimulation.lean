import Init

/- P40-MATH-B-P5. A consciously restricted HEAD routing policy model.
   Go functions and client observations are checked separately by native tests.
   These theorems establish semantics of this declared model, not equivalence
   with the full Echo, Gin or Go operational semantics. No axiom/sorry/admit. -/
namespace P40IssueSimulation

inductive HeadTarget where
 | direct
 | fallback
 | unavailable
 deriving Repr, DecidableEq

structure NativeSourceState where
 directHead : Bool
 registeredGet : Bool
 autoHead : Bool
 getInvocations : Nat
 hiddenRevision : Nat
 deriving Repr, DecidableEq

structure BoundarySummary where
 hasDirect : Bool
 hasFallback : Bool
 getInvocations : Nat
 deriving Repr, DecidableEq

def abstract (s : NativeSourceState) : BoundarySummary :=
 { hasDirect := s.directHead
   hasFallback := s.autoHead && s.registeredGet
   getInvocations := s.getInvocations }

def sourceDispatch (s : NativeSourceState) : HeadTarget :=
 if s.directHead then .direct
 else if s.autoHead && s.registeredGet then .fallback
 else .unavailable

def abstractDispatch (a : BoundarySummary) : HeadTarget :=
 if a.hasDirect then .direct
 else if a.hasFallback then .fallback
 else .unavailable

theorem head_dispatch_refines (s : NativeSourceState) :
    sourceDispatch s = abstractDispatch (abstract s) := by
  cases s with
  | mk d g a visits noise =>
    cases d <;> cases g <;> cases a <;>
      simp [sourceDispatch, abstractDispatch, abstract]

def sourceHeadStep (s : NativeSourceState) : NativeSourceState :=
 { s with
   getInvocations := s.getInvocations +
     (if sourceDispatch s = .fallback then 1 else 0)
   hiddenRevision := s.hiddenRevision + 1 }

def abstractHeadStep (a : BoundarySummary) : BoundarySummary :=
 { a with
   getInvocations := a.getInvocations +
     (if abstractDispatch a = .fallback then 1 else 0) }

theorem one_step_commutes (s : NativeSourceState) :
    abstract (sourceHeadStep s) = abstractHeadStep (abstract s) := by
  cases s with
  | mk d g a visits noise =>
    cases d <;> cases g <;> cases a <;>
      simp [abstract, sourceHeadStep, abstractHeadStep,
            sourceDispatch, abstractDispatch]

def runSource : Nat → NativeSourceState → NativeSourceState
 | 0, s => s
 | n+1, s => runSource n (sourceHeadStep s)

def runAbstract : Nat → BoundarySummary → BoundarySummary
 | 0, s => s
 | n+1, s => runAbstract n (abstractHeadStep s)

theorem head_finite_simulation (n : Nat) (s : NativeSourceState) :
    abstract (runSource n s) = runAbstract n (abstract s) := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
      change abstract (runSource n (sourceHeadStep s)) =
        runAbstract n (abstractHeadStep (abstract s))
      rw [ih (sourceHeadStep s), one_step_commutes s]

theorem opaque_revision_irrelevant (s : NativeSourceState) (r : Nat) :
    abstract {s with hiddenRevision := r} = abstract s := by
  rfl

theorem bounded_future_revision_abstract_equivalence
    (s : NativeSourceState) (r n : Nat) :
    abstract (runSource n {s with hiddenRevision := r}) =
    abstract (runSource n s) := by
  rw [head_finite_simulation, head_finite_simulation]
  rw [opaque_revision_irrelevant]

def explicitExample : NativeSourceState :=
 { directHead := true, registeredGet := true, autoHead := true,
   getInvocations := 0, hiddenRevision := 7 }

def fallbackExample : NativeSourceState :=
 { directHead := false, registeredGet := true, autoHead := true,
   getInvocations := 0, hiddenRevision := 7 }

def defaultExample : NativeSourceState :=
 { fallbackExample with autoHead := false }

theorem explicit_handler_priority :
    sourceDispatch explicitExample = .direct := by decide

theorem enabled_auto_head_executes_get :
    sourceDispatch fallbackExample = .fallback ∧
    (sourceHeadStep fallbackExample).getInvocations = 1 := by decide

theorem opt_out_prevents_get_head_fallback :
    sourceDispatch defaultExample = .unavailable := by decide

theorem source_revision_not_required_for_sufficient_head_boundary :
    abstract {fallbackExample with hiddenRevision := 222} =
    abstract fallbackExample := by decide


/- Restricted observational irredundancy: HEAD status and empty response body
   cannot identify whether GET-handler side effects execute. This remains a
   classical no-factorization fact; original source cases are checked in Go. -/
def statusBodyOnly (s : NativeSourceState) : Nat × Bool :=
  if sourceDispatch s = .unavailable then (405, true) else (200, true)

def getExecuted (s : NativeSourceState) : Bool :=
  decide (sourceDispatch s = .fallback)

theorem status_body_same_for_explicit_and_fallback :
    statusBodyOnly explicitExample = statusBodyOnly fallbackExample := by decide

theorem handler_effect_differs_for_explicit_and_fallback :
    getExecuted explicitExample ≠ getExecuted fallbackExample := by decide

theorem no_status_body_only_handler_effect_classifier :
    ¬ ∃ f : Nat × Bool → Bool,
        ∀ s : NativeSourceState, getExecuted s = f (statusBodyOnly s) := by
  intro h
  rcases h with ⟨f, hf⟩
  apply handler_effect_differs_for_explicit_and_fallback
  calc
    getExecuted explicitExample = f (statusBodyOnly explicitExample) := hf _
    _ = f (statusBodyOnly fallbackExample) := by
      rw [status_body_same_for_explicit_and_fallback]
    _ = getExecuted fallbackExample := (hf _).symm


end P40IssueSimulation
