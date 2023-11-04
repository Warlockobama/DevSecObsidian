
# Buffer Overflow

**ID:** 30001
**Risk Level:** Medium
**CWE ID:** 120
**WASC ID:** 7
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Buffer overflow errors are characterized by the overwriting of memory spaces of the background web process, which should have never been modified intentionally or unintentionally. Overwriting values of the IP (Instruction Pointer), BP (Base Pointer) and other registers causes exceptions, segmentation faults, and other process errors to occur. Usually these errors end execution of the application in an unexpected way.

## Solution
Rewrite the background program using proper return length checking.  This will require a recompile of the background executable.

## References
https://owasp.org/www-community/attacks/Buffer_overflow_attack
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/BufferOverflowScanRule.java
