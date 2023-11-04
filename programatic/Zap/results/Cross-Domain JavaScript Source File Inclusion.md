
# Cross-Domain JavaScript Source File Inclusion

**ID:** 10017
**Risk Level:** Low
**CWE ID:** 829
**WASC ID:** 15
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The page includes one or more script files from a third-party domain.

## Solution
Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CrossDomainScriptInclusionScanRule.java
