
# Verification Request Identified

**ID:** 10113
**Risk Level:** Informational
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The given request has been identified as a good candidate for authentication verification. If the request is in a context which has a Verification Strategy set to "Poll" but where the URL is empty then this rule will fill in the correct values.

## Solution
This is an informational alert rather than a vulnerability and so there is nothing to fix.

## References
https://www.zaproxy.org/docs/desktop/addons/authentication-helper/verif-id
https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/VerificationDetectionScanRule.java
