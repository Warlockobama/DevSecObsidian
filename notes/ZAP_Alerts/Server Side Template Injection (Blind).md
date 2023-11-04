
# Server Side Template Injection (Blind)

**ID:** 90036
**Risk Level:** Not specified
**CWE ID:** 74
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Server Side Template Injection (Blind)"
alertid: 90036
alertindex: 9003600
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: High
solution: "Instead of inserting the user input in the template, use it as rendering argument."
references:
   - https://portswigger.net/blog/server-side-template-injection
other: ""
cwe: 74
wasc: 20
alerttags: 
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SstiBlindScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/SstiBlindScanRule.java"
---
When the user input is inserted in the template instead of being used as argument in rendering is evaluated by the template engine. Depending on the template engine it can lead to remote code execution.


## Solution
No solution provided.

## References
No references provided.
