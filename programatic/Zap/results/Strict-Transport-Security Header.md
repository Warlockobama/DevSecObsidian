
# Strict-Transport-Security Header

**ID:** 10035
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

## Solution
Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

## References
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html
https://owasp.org/www-community/Security_Headers
http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
http://caniuse.com/stricttransportsecurity
http://tools.ietf.org/html/rfc6797
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java
