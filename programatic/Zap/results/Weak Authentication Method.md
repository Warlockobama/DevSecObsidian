
# Weak Authentication Method

**ID:** 10105
**Risk Level:** Not specified
**CWE ID:** 326
**WASC ID:** 4
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
HTTP basic or digest authentication has been used over an unsecured connection. The credentials can be read and then reused by someone with access to the network.

## Solution
Protect the connection using HTTPS or use a stronger authentication mechanism

## References
https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java
