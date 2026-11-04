# Immutable original R2 CI failure and correction

The first R2 native workflow at commit 6e8ef3783eb1ba30638e74054c3bda97cb9b2567 produced failed GitHub run #41758875735 with **zero jobs**: invalid YAML because a step-name contained an unquoted colon (Formal classical rival: test, vet, race). Python PyYAML independently confirmed the syntax issue.

The exact minimal correction at commit 245f311e374c2ca168e7d64d14e8fafa78d636fe quotes the step name. GitHub recognized a normal run #41758962571 with QUEUED status. This is workflow admission recovery, not success of any new original-source test.

Follow-up R2 static source oracle source files and tests were added after the initial recovery. The R2 workflow must be updated to include static tests, and later success must be tied to the exact tested commit. Preserve the failed run permanently.
