
# HTTP Parameter Pollution

**ID:** 20014
**Risk Level:** Not specified
**CWE ID:** 20
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "HTTP Parameter Pollution"
alertid: 20014
alertindex: 2001400
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Informational
solution: "Properly sanitize the user input for parameter delimiters"
references:
   - http://www.google.com/search?q=http+parameter+pollution
other: ""
cwe: 20
wasc: 20
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
  - WSTG-v42-INPV-04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttpParameterPollutionScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/HttpParameterPollutionScanRule.java"
---
HTTP Parameter Pollution (HPP) attacks consist of injecting encoded query string delimiters into other existing parameters. If a web application does not properly sanitize the user input, a malicious user can compromise the logic of the application to perform either client-side or server-side attacks. One consequence of HPP attacks is that the attacker can potentially override existing hard-coded HTTP parameters to modify the behavior of an application, bypass input validation checkpoints, and access and possibly exploit variables that may be out of direct reach.


## Solution
No solution provided.

## References
No references provided.
