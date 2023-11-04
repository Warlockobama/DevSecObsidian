
# Hash Disclosure

**ID:** 10097
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A hash was disclosed by the web server.

## Solution
Ensure that hashes that are used to protect credentials or other resources are not leaked by the web server or database. There is typically no requirement for password hashes to be accessible to the web browser.      

## References
http://projects.webappsec.org/w/page/13246936/Information%20Leakage
http://openwall.info/wiki/john/sample-hashes
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java
