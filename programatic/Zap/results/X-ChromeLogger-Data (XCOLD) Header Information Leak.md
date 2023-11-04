
# X-ChromeLogger-Data (XCOLD) Header Information Leak

**ID:** 10052
**Risk Level:** Medium
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The server is leaking information through the X-ChromeLogger-Data (or X-ChromePhp-Data) response header. The content of such headers can be customized by the developer, however it is not uncommon to find: server file system locations, vhost declarations, etc.

## Solution
Disable this functionality in Production when it might leak information that could be leveraged by an attacker. Alternatively ensure that use of the functionality is tied to a strong authorization check and only available to administrators or support personnel for troubleshooting purposes not general users.

## References
https://craig.is/writing/chrome-logger
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XChromeLoggerDataInfoLeakScanRule.java
