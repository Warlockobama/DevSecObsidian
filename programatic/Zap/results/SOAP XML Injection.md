
# SOAP XML Injection

**ID:** 90029
**Risk Level:** High
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Some XML injected code has been interpreted by the server.

## Solution
Use a detailed description of SOAP attributes in the WSDL file.

## References
http://www.ws-attacks.org/index.php/XML_Injection
https://github.com/zaproxy/zap-extensions/blob/main/addOns/soap/src/main/java/org/zaproxy/zap/extension/soap/SOAPXMLInjectionActiveScanRule.java
