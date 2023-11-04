
# SOAP Action Spoofing

**ID:** 90026
**Risk Level:** High
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
An unintended SOAP operation was executed by the server.

## Solution
If not required, the SOAPAction attribute should be disabled. If needed, the operation within the SOAPAction and the SOAP body should always be compared before executing any operation. Any mismatch should be regarded as an attack.

## References
http://www.ws-attacks.org/index.php/SOAPAction_Spoofing
https://github.com/zaproxy/zap-extensions/blob/main/addOns/soap/src/main/java/org/zaproxy/zap/extension/soap/SOAPActionSpoofingActiveScanRule.java
