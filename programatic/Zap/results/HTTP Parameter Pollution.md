
# HTTP Parameter Pollution

**ID:** 20014
**Risk Level:** Informational
**CWE ID:** 20
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
HTTP Parameter Pollution (HPP) attacks consist of injecting encoded query string delimiters into other existing parameters. If a web application does not properly sanitize the user input, a malicious user can compromise the logic of the application to perform either client-side or server-side attacks. One consequence of HPP attacks is that the attacker can potentially override existing hard-coded HTTP parameters to modify the behavior of an application, bypass input validation checkpoints, and access and possibly exploit variables that may be out of direct reach.

## Solution
Properly sanitize the user input for parameter delimiters

## References
http://www.google.com/search?q=http+parameter+pollution
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/HttpParameterPollutionScanRule.java
