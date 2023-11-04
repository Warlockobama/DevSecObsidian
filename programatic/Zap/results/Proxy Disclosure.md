
# Proxy Disclosure

**ID:** 40025
**Risk Level:** Medium
**CWE ID:** 200
**WASC ID:** 45
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description


## Solution
Disable the 'TRACE' method on the proxy servers, as well as the origin web/application server. Disable the 'OPTIONS' method on the proxy servers, as well as the origin web/application server, if it is not required for other purposes, such as 'CORS' (Cross Origin Resource Sharing). Configure the web and application servers with custom error pages, to prevent 'fingerprintable' product-specific error pages being leaked to the user in the event of HTTP errors, such as 'TRACK' requests for non-existent pages. Configure all proxies, application servers, and web servers to prevent disclosure of the technology and version information in the 'Server' and 'X-Powered-By' HTTP response headers. 

## References
https://tools.ietf.org/html/rfc7231#section-5.1.2
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ProxyDisclosureScanRule.java
