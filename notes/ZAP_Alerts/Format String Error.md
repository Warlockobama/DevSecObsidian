
# Format String Error

**ID:** 30002
**Risk Level:** Not specified
**CWE ID:** 134
**WASC ID:** 6
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Format String Error"
alertid: 30002
alertindex: 3000200
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Rewrite the background program using proper deletion of bad character strings.  This will require a recompile of the background executable."
references:
   - https://owasp.org/www-community/attacks/Format_string_attack
other: "Potential Format String Error.  The script closed the connection on a /%s"
cwe: 134
wasc: 6
techtags: 
  - Language.C
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/FormatStringScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/FormatStringScanRule.java"
---
A Format String error occurs when the submitted data of an input string is evaluated as a command by the application. 


## Solution
No solution provided.

## References
No references provided.
