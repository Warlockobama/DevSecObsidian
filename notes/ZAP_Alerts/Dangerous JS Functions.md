
# Dangerous JS Functions

**ID:** 10110
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Dangerous JS Functions"
alertid: 10110
alertindex: 1011000
alerttype: "Passive"
alertcount: 1
status: beta
type: alert
risk: Low
solution: "See the references for security advice on the use of these functions."
references:
   - https://angular.io/guide/security
other: ""
cwe: 749
alerttags: 
  - CUSTOM_PAYLOADS
  - OWASP_2021_A04
  - WSTG-v42-CLNT-02
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/JsFunctionScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrulesBeta/JsFunctionScanRule.java"
---
A dangerous JS function seems to be in use that would leave the site vulnerable.


## Solution
No solution provided.

## References
No references provided.
