
# Hash Disclosure

**ID:** 10097
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Hash Disclosure"
alertid: 10097
alertindex: 1009700
alerttype: "Passive"
alertcount: 1
status: release
type: alert
solution: "Ensure that hashes that are used to protect credentials or other resources are not leaked by the web server or database. There is typically no requirement for password hashes to be accessible to the web browser.      "
references:
   - http://projects.webappsec.org/w/page/13246936/Information%20Leakage
   - http://openwall.info/wiki/john/sample-hashes
other: ""
alerttags: 
  - OWASP_2017_A03
  - OWASP_2021_A04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java"
---
A hash was disclosed by the web server.


## Solution
No solution provided.

## References
No references provided.
