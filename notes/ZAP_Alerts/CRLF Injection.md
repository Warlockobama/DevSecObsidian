
# CRLF Injection

**ID:** 40003
**Risk Level:** Not specified
**CWE ID:** 113
**WASC ID:** 25
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "CRLF Injection"
alertid: 40003
alertindex: 4000300
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Type check the submitted parameter carefully.  Do not allow CRLF to be injected by filtering CRLF."
references:
   - http://www.watchfire.com/resources/HTTPResponseSplitting.pdf
   - http://webappfirewall.com/lib/crlf-injection.txtnull
   - http://www.securityfocus.com/bid/9804
other: ""
cwe: 113
wasc: 25
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
  - WSTG-v42-INPV-15
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrlfInjectionScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/CrlfInjectionScanRule.java"
---
Cookie can be set via CRLF injection.  It may also be possible to set arbitrary HTTP response headers. In addition, by carefully crafting the injected response using cross-site script, cache poisoning vulnerability may also exist.


## Solution
No solution provided.

## References
No references provided.
