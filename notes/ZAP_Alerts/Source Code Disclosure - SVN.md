
# Source Code Disclosure - SVN

**ID:** 42
**Risk Level:** Not specified
**CWE ID:** 541
**WASC ID:** 34
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Source Code Disclosure - SVN"
alertid: 42
alertindex: 4200
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: "Ensure that SVN metadata files are not deployed to the web server or application server"
references:
   - http://projects.webappsec.org/Predictable-Resource-Location
   - https://cwe.mitre.org/data/definitions/425.html
other: ""
cwe: 541
wasc: 34
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/SourceCodeDisclosureSvnScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/SourceCodeDisclosureSvnScanRule.java"
---
The source code for the current page was disclosed by the web server.


## Solution
No solution provided.

## References
No references provided.
