
# Authentication Request Identified

**ID:** 10111
**Risk Level:** Informational
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.

## Solution
This is an informational alert rather than a vulnerability and so there is nothing to fix.

## References
https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/AuthenticationDetectionScanRule.java
