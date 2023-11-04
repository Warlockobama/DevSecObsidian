
# Server Side Request Forgery

**ID:** 40046
**Risk Level:** High
**CWE ID:** 918
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The web server receives a remote address and retrieves the contents of this URL, but it does not sufficiently ensure that the request is being sent to the expected destination.

## Solution
Do not accept remote addresses as request parameters, and if you must, ensure that they are validated against an allow-list of expected values.

## References
https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/SsrfScanRule.java
