
# Httpoxy - Proxy Header Misuse

**ID:** 10107
**Risk Level:** High
**CWE ID:** 20
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The server initiated a proxied request via the proxy specified in the HTTP Proxy header of the request.Httpoxy typically affects code running in CGI or CGI like environments.
This may allow attackers to:
* Proxy the outgoing HTTP requests made by the web application
* Direct the server to open outgoing connections to an address and port of their choosing or
* Tie up server resources by forcing the vulnerable software to use a malicious proxy

## Solution
The best immediate mitigation is to block Proxy request headers as early as possible, and before they hit your application.

## References
https://httpoxy.org/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttPoxyScanRule.java
