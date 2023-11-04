
# Server Side Template Injection

**ID:** 90035
**Risk Level:** Not specified
**CWE ID:** 94
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Server Side Template Injection"
alertid: 90035
alertindex: 9003500
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: High
solution: "Instead of inserting the user input in the template, use it as rendering argument."
references:
   - https://portswigger.net/blog/server-side-template-injection
other: ""
cwe: 94
wasc: 20
alerttags: 
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SstiScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/SstiScanRule.java"
---
When the user input is inserted in the template instead of being used as argument in rendering is evaluated by the template engine. Depending on the template engine it can lead to remote code execution.


## Solution
No solution provided.

## References
No references provided.
