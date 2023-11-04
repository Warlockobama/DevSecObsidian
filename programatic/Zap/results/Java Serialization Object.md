
# Java Serialization Object

**ID:** 90002
**Risk Level:** Medium
**CWE ID:** 502
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
Java Serialization seems to be in use. If not correctly validated, an attacker can send a specially crafted object. This can lead to a dangerous "Remote Code Execution". A magic sequence identifying JSO has been detected (Base64: rO0AB, Raw: 0xac, 0xed, 0x00, 0x05).

## Solution
Deserialization of untrusted data is inherently dangerous and should be avoided.

## References
https://www.oracle.com/java/technologies/javase/seccodeguide.html#8
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/JsoScanRule.java
