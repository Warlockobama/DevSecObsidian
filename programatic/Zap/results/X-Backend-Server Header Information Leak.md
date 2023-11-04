
# X-Backend-Server Header Information Leak

**ID:** 10039
**Risk Level:** Low
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The server is leaking information pertaining to backend systems (such as hostnames or IP addresses). Armed with this information an attacker may be able to attack other systems or more directly/efficiently attack those systems.

## Solution
Ensure that your web server, application server, load balancer, etc. is configured to suppress X-Backend-Server headers.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XBackendServerInformationLeakScanRule.java
