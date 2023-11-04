
# HTTPS Content Available via HTTP

**ID:** 10047
**Risk Level:** Low
**CWE ID:** 311
**WASC ID:** 4
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Content which was initially accessed via HTTPS (i.e.: using SSL/TLS encryption) is also accessible via HTTP (without encryption).

## Solution
Ensure that your web server, application server, load balancer, etc. is configured to only serve such content via HTTPS. Consider implementing HTTP Strict Transport Security.

## References
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html
https://owasp.org/www-community/Security_Headers
http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
http://caniuse.com/stricttransportsecurity
http://tools.ietf.org/html/rfc6797
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttpsAsHttpScanRule.java
