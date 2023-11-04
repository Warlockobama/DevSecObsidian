
# Hidden File Found

**ID:** 40035
**Risk Level:** Medium
**CWE ID:** 538
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.

## Solution
Consider whether or not the component is actually required in production, if it isn't then disable it. If it is then ensure access to it requires appropriate authentication and authorization, or limit exposure to internal systems or specific source IPs, etc.

## References
https://blog.hboeck.de/archives/892-Introducing-Snallygaster-a-Tool-to-Scan-for-Secrets-on-Web-Servers.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/HiddenFilesScanRule.java
