
# HTTPS to HTTP Insecure Transition in Form Post

**ID:** 10042
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
This check identifies secure HTTPS pages that host insecure HTTP forms. The issue is that a secure page is transitioning to an insecure page when data is uploaded through a form. The user may think they're submitting data to a secure page when in fact they are not.

## Solution
Ensure sensitive data is only sent over secured HTTPS channels.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureFormPostScanRule.java
