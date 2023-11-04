
# Timestamp Disclosure

**ID:** 10096
**Risk Level:** Low
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A timestamp was disclosed by the application/web server

## Solution
Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

## References
http://projects.webappsec.org/w/page/13246936/Information%20Leakage
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/TimestampDisclosureScanRule.java
