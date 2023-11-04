
# Session Management Response Identified

**ID:** 10112
**Risk Level:** Informational
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

## Solution
This is an informational alert rather than a vulnerability and so there is nothing to fix.

## References
https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id
https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/SessionDetectionScanRule.java
