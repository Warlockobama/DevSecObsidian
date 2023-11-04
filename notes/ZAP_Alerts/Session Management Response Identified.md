
# Session Management Response Identified

**ID:** 10112
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Session Management Response Identified"
alertid: 10112
alertindex: 1011200
alerttype: "Passive"
alertcount: 1
status: beta
type: alert
risk: Informational
solution: "This is an informational alert rather than a vulnerability and so there is nothing to fix."
references:
   - https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id
other: " header:authorization"
alerttags: 
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/authhelper/src/main/java/org/zaproxy/addon/authhelper/SessionDetectionScanRule.java
linktext: "org/zaproxy/addon/authhelper/SessionDetectionScanRule.java"
---
The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.


## Solution
No solution provided.

## References
No references provided.
