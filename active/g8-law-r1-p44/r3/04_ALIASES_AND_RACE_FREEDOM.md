# Aliasing can violate temporal semantics while remaining race-free

App store has mutex-protected mutable string value, accessed only under lock. Under LiveAlias middleware stores a pointer to Shared in the request's context View; handler later calls Shared.Value and can see a concurrent POST update performed after the pointer was captured. Under FrozenValue middleware reads Shared.Value while the lock is held by Value, copies the immutable string into View and the later handler reads that copied string.

Both choices are data-race-free (read/write synchronizes through Shared.mu). Only FrozenValue satisfies the D1 snapshot contract under the fixed happens-before schedule. A Go race detector PASS is therefore not evidence of the higher-level temporal property.

This is familiar alias analysis and concurrency semantics, not a novel EAC law. An equal-information classical alias/happens-before rival predicts all cases and the one-unit app capture repair.
