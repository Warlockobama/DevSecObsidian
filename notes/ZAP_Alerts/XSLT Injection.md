
# XSLT Injection

**ID:** 90017
**Risk Level:** Not specified
**CWE ID:** 91
**WASC ID:** 23
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "XSLT Injection"
alertid: 90017
alertindex: 9001700
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Sanitize and analyze every user input coming from any client-side."
references:
   - https://www.contextis.com/blog/xslt-server-side-injection-attacks
other: ""
cwe: 91
wasc: 23
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/XsltInjectionScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/XsltInjectionScanRule.java"
---
Injection using XSL transformations may be possible, and may allow an attacker to read system information, read and write files, or execute arbitrary code.


## Solution
No solution provided.

## References
No references provided.
