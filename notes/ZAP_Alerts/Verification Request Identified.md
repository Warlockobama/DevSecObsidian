
# Verification Request Identified

**ID:** 10113
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Verification Request Identified"
alertid: 10113
alertindex: 1011300
alerttype: "Passive"
alertcount: 1
status: beta
type: alert
risk: Informational
solution: "This is an informational alert rather than a vulnerability and so there is nothing to fix."
references:
   - https://www.zaproxy.org/docs/desktop/addons/authentication-helper/verif-id
other: ""
alerttags: 
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/VerificationDetectionScanRule.java
linktext: "org/zaproxy/addon/authhelper/VerificationDetectionScanRule.java"
---
The given request has been identified as a good candidate for authentication verification. If the request is in a context which has a Verification Strategy set to "Poll" but where the URL is empty then this rule will fill in the correct values.


## Solution
No solution provided.

## References
No references provided.
