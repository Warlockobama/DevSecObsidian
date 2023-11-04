
# Cookie No HttpOnly Flag

**ID:** 10010
**Risk Level:** Low
**CWE ID:** 1004
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

## Solution
Ensure that the HttpOnly flag is set for all cookies.

## References
https://owasp.org/www-community/HttpOnly
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieHttpOnlyScanRule.java
