
# Content-Type Header Missing

**ID:** 10019
**Risk Level:** Informational
**CWE ID:** 345
**WASC ID:** 12
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The Content-Type header was either missing or empty.

## Solution
Ensure each page is setting the specific and appropriate content-type value for the content being delivered.

## References
http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ContentTypeMissingScanRule.java
