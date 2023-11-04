
# Big Redirect Detected (Potential Sensitive Information Leak)

**ID:** 10044
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The server has responded with a redirect that seems to provide a large response. This may indicate that although the server sent a redirect it also responded with body content (which may include sensitive details, PII, etc.).

## Solution
Ensure that no sensitive information is leaked via redirect responses. Redirect responses should have almost no content.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/BigRedirectsScanRule.java
