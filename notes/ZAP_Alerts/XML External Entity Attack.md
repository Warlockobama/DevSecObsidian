
# XML External Entity Attack

**ID:** 90023
**Risk Level:** Not specified
**CWE ID:** 611
**WASC ID:** 43
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "XML External Entity Attack"
alertid: 90023
alertindex: 9002300
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: High
solution: ""
references:
   - http://projects.webappsec.org/XML-External-Entities
other: ""
cwe: 611
wasc: 43
alerttags: 
  - OWASP_2017_A04
  - OWASP_2021_A03
  - WSTG-v42-INPV-07
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/XxeScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/XxeScanRule.java"
---
This technique takes advantage of a feature of XML to build documents dynamically at the time of processing. An XML message can either provide data explicitly or by pointing to an URI where the data exists. In the attack technique, external entities may replace the entity value with malicious data, alternate referrals or may compromise the security of the data the server/XML application has access to.
	Attackers may also use External Entities to have the web services server download malicious code or content to the server for use in secondary or follow on attacks.


## Solution
No solution provided.

## References
No references provided.
