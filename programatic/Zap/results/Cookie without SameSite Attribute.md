
# Cookie without SameSite Attribute

**ID:** 10054
**Risk Level:** Low
**CWE ID:** 1275
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

## Solution
Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.

## References
https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieSameSiteScanRule.java
