
# Information Disclosure - Suspicious Comments

**ID:** 10027
**Risk Level:** Informational
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.

## Solution
Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InformationDisclosureSuspiciousCommentsScanRule.java
