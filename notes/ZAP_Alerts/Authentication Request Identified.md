
# Authentication Request Identified

**ID:** 10111
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Authentication Request Identified"
alertid: 10111
alertindex: 1011100
alerttype: "Passive"
alertcount: 1
status: beta
type: alert
risk: Informational
solution: "This is an informational alert rather than a vulnerability and so there is nothing to fix."
references:
   - https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/
other: "userParam=username userValue=test passwordParam=password"
alerttags: 
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/AuthenticationDetectionScanRule.java
linktext: "org/zaproxy/addon/authhelper/AuthenticationDetectionScanRule.java"
---
The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.


## Solution
No solution provided.

## References
No references provided.
