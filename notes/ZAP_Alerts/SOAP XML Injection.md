
# SOAP XML Injection

**ID:** 90029
**Risk Level:** Not specified
**CWE ID:** 0
**WASC ID:** 0
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "SOAP XML Injection"
alertid: 90029
alertindex: 9002900
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: High
solution: "Use a detailed description of SOAP attributes in the WSDL file."
references:
   - http://www.ws-attacks.org/index.php/XML_Injection
other: "Some XML injected code has been interpreted by the server."
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/soap/src/main/java/org/zaproxy/zap/extension/soap/SOAPXMLInjectionActiveScanRule.java
linktext: "org/zaproxy/zap/extension/soap/SOAPXMLInjectionActiveScanRule.java"
---
Some XML injected code has been interpreted by the server.


## Solution
No solution provided.

## References
No references provided.
