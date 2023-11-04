
# HTTP Parameter Override

**ID:** 10026
**Risk Level:** Medium
**CWE ID:** 20
**WASC ID:** 20
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
Unspecified form action: HTTP parameter override attack potentially possible. This is a known problem with Java Servlets but other platforms may also be vulnerable.

## Solution
All forms must specify the action URL.

## References
https://download.oracle.com/javaee-archive/servlet-spec.java.net/jsr340-experts/att-0317/OnParameterPollutionAttacks.pdf
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/ServletParameterPollutionScanRule.java
