
# PII Disclosure

**ID:** 10062
**Risk Level:** High
**CWE ID:** 359
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The response contains Personally Identifiable Information, such as CC number, SSN and similar sensitive data.

## Solution
Check the response for the potential presence of personally identifiable information (PII), ensure nothing sensitive is leaked by the application.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PiiScanRule.java
