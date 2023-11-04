
# Sub Resource Integrity Attribute Missing

**ID:** 90003
**Risk Level:** Medium
**CWE ID:** 345
**WASC ID:** 15
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The integrity attribute is missing on a script or link tag served by an external server. The integrity tag prevents an attacker who have gained access to this server from injecting a malicious content.

## Solution
Provide a valid integrity attribute to the tag.

## References
https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/SubResourceIntegrityAttributeScanRule.java
