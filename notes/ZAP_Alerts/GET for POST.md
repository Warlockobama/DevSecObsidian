
# GET for POST

**ID:** 10058
**Risk Level:** Not specified
**CWE ID:** 16
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "GET for POST"
alertid: 10058
alertindex: 1005800
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Informational
solution: "Ensure that only POST is accepted where POST is expected."
other: ""
cwe: 16
wasc: 20
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A04
  - WSTG-v42-CONF-06
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java"
---
A request that was originally observed as a POST was also accepted as a GET. This issue does not represent a security weakness unto itself, however, it may facilitate simplification of other attacks. For example if the original POST is subject to Cross-Site Scripting (XSS), then this finding may indicate that a simplified (GET based) XSS may also be possible.


## Solution
No solution provided.

## References
No references provided.
