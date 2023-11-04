
# HTTP Only Site

**ID:** 10106
**Risk Level:** Medium
**CWE ID:** 311
**WASC ID:** 4
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The site is only served under HTTP and not HTTPS.

## Solution
Configure your web or application server to use SSL (https).

## References
https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
https://letsencrypt.org/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttpOnlySiteScanRule.java
