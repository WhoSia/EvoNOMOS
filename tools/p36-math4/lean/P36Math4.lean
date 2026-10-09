import Init

/-!
P36-MATH-4. Ordinary deterministic transition-system homomorphism.
A conditional classical theorem, not a discovered software-structure law.
Original-Go repairs provide separate evidence that the assumptions
sometimes hold or fail; there is no universal source-to-state model here.
-/

namespace EvoNOMOS.P36.MATH4

universe u v w z

def traceRun {State : Type u} {Action : Type v}
    (step : State → Action → State) : State → List Action → State
  | current, [] => current
  | current, action :: remainder =>
      traceRun step (step current action) remainder

theorem forgetful_simulation_preserves_every_finite_trace
    {Rich : Type u} {Bare : Type v} {Action : Type w}
    (project : Rich → Bare)
    (richStep : Rich → Action → Rich)
    (bareStep : Bare → Action → Bare)
    (respectsStep :
       ∀ (s : Rich) (a : Action),
         project (richStep s a) = bareStep (project s) a) :
    ∀ (s : Rich) (actions : List Action),
      project (traceRun richStep s actions) =
      traceRun bareStep (project s) actions := by
  intro s actions
  induction actions generalizing s with
  | nil =>
      rfl
  | cons action rest ih =>
      change project (traceRun richStep (richStep s action) rest) =
        traceRun bareStep (bareStep (project s) action) rest
      rw [ih (richStep s action)]
      rw [respectsStep s action]

theorem forgetful_simulation_preserves_observed_traces
    {Rich : Type u} {Bare : Type v} {Action : Type w} {Output : Type z}
    (project : Rich → Bare)
    (richStep : Rich → Action → Rich)
    (bareStep : Bare → Action → Bare)
    (richObserve : Rich → Output)
    (bareObserve : Bare → Output)
    (respectsStep :
       ∀ (s : Rich) (a : Action),
         project (richStep s a) = bareStep (project s) a)
    (respectsObservation :
       ∀ (s : Rich), richObserve s = bareObserve (project s)) :
    ∀ (s : Rich) (actions : List Action),
      richObserve (traceRun richStep s actions) =
      bareObserve (traceRun bareStep (project s) actions) := by
  intro s actions
  calc
    richObserve (traceRun richStep s actions) =
      bareObserve (project (traceRun richStep s actions)) :=
        respectsObservation (traceRun richStep s actions)
    _ = bareObserve (traceRun bareStep (project s) actions) :=
        congrArg bareObserve
          (forgetful_simulation_preserves_every_finite_trace
            project richStep bareStep respectsStep s actions)

end EvoNOMOS.P36.MATH4
