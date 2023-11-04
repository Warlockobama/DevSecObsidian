
# Remote Code Execution - Shell Shock

**ID:** 10048
**Risk Level:** Not specified
**CWE ID:** 78
**WASC ID:** 31
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Remote Code Execution - Shell Shock"
alertid: 10048
alertindex: 1004800
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: High
solution: "Update Bash on the server to the latest version"
references:
   - http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271
   - http://www.troyhunt.com/2014/09/everything-you-need-to-know-about.html
other: ""
cwe: 78
wasc: 31
alerttags: 
  - OWASP_2017_A09
  - OWASP_2021_A06
  - WSTG-v42-INPV-12
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ShellShockScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/ShellShockScanRule.java"
---
The server is running a version of the Bash shell that allows remote attackers to execute arbitrary code 


## Solution
No solution provided.

## References
No references provided.
