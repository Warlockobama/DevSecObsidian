
# Parameter Tampering

**ID:** 40008
**Risk Level:** Medium
**CWE ID:** 472
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Parameter manipulation caused an error page or Java stack trace to be displayed.  This indicated lack of exception handling and potential areas for further exploit.

## Solution
Identify the cause of the error and fix it.  Do not trust client side input and enforce a tight check in the server side.  Besides, catch the exception properly.  Use a generic 500 error page for internal server error.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ParameterTamperScanRule.java
