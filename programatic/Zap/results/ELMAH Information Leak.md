
# ELMAH Information Leak

**ID:** 40028
**Risk Level:** Medium
**CWE ID:** 94
**WASC ID:** 14
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The Error Logging Modules and Handlers (ELMAH [elmah.axd]) HTTP Module was found to be available. This module can leak a significant amount of valuable information.

## Solution
Consider whether or not ELMAH is actually required in production, if it isn't then disable it. If it is then ensure access to it requires authentication and authorization. See also: https://elmah.github.io/a/securing-error-log-pages/

## References
https://www.troyhunt.com/aspnet-session-hijacking-with-google/
https://www.nuget.org/packages/elmah
https://elmah.github.io/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ElmahScanRule.java
