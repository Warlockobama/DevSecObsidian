
# Generic Padding Oracle

**ID:** 90024
**Risk Level:** High
**CWE ID:** 209
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
By manipulating the padding on an encrypted string, an attacker is able to generate an error message that indicates a likely 'padding oracle' vulnerability. Such a vulnerability can affect any application or framework that uses encryption improperly, such as some versions of ASP.net, Java Server Faces, and Mono. An attacker may exploit this issue to decrypt data and recover encryption keys, potentially viewing and modifying confidential data. This rule should detect the MS10-070 padding oracle vulnerability in ASP.net if CustomErrors are enabled for that.

## Solution
Update the affected server software, or modify the scripts so that they properly validate encrypted data before attempting decryption.

## References
http://netifera.com/research/
http://www.microsoft.com/technet/security/bulletin/ms10-070.mspx
http://www.mono-project.com/Vulnerabilities#ASP.NET_Padding_Oracle
https://bugzilla.redhat.com/show_bug.cgi?id=623799
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PaddingOracleScanRule.java
