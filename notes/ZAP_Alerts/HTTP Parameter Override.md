
# HTTP Parameter Override

**ID:** 10026
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "HTTP Parameter Override"
alertid: 10026
alertindex: 1002600
alerttype: "Passive"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: "All forms must specify the action URL."
references:
   - https://download.oracle.com/javaee-archive/servlet-spec.java.net/jsr340-experts/att-0317/OnParameterPollutionAttacks.pdf
other: ""
cwe: 20
wasc: 20
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/ServletParameterPollutionScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrulesBeta/ServletParameterPollutionScanRule.java"
---
Unspecified form action: HTTP parameter override attack potentially possible. This is a known problem with Java Servlets but other platforms may also be vulnerable.


## Solution
No solution provided.

## References
No references provided.
