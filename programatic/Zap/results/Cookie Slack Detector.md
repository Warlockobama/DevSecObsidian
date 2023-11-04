
# Cookie Slack Detector

**ID:** 90027
**Risk Level:** Informational
**CWE ID:** 200
**WASC ID:** 45
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Repeated GET requests: drop a different cookie each time, followed by normal request with all cookies to stabilize session, compare responses against original baseline GET. This can reveal areas where cookie based authentication/attributes are not actually enforced.

## Solution


## References
http://projects.webappsec.org/Fingerprinting
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/SlackerCookieScanRule.java
