
# SOAP Action Spoofing

**ID:** 90026
**Risk Level:** Not specified
**CWE ID:** 0
**WASC ID:** 0
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "SOAP Action Spoofing"
alertid: 90026
alertindex: 9002600
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: High
solution: "If not required, the SOAPAction attribute should be disabled. If needed, the operation within the SOAPAction and the SOAP body should always be compared before executing any operation. Any mismatch should be regarded as an attack."
references:
   - http://www.ws-attacks.org/index.php/SOAPAction_Spoofing
other: "An unintended SOAP operation was executed by the server."
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/soap/src/main/java/org/zaproxy/zap/extension/soap/SOAPActionSpoofingActiveScanRule.java
linktext: "org/zaproxy/zap/extension/soap/SOAPActionSpoofingActiveScanRule.java"
---
An unintended SOAP operation was executed by the server.


## Solution
No solution provided.

## References
No references provided.
