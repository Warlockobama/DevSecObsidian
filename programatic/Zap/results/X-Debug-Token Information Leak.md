
# X-Debug-Token Information Leak

**ID:** 10056
**Risk Level:** Low
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The response contained an X-Debug-Token or X-Debug-Token-Link header. This indicates that Symfony's Profiler may be in use and exposing sensitive data.

## Solution
Limit access to Symfony's Profiler, either via authentication/authorization or limiting inclusion of the header to specific clients (by IP, etc.).

## References
https://symfony.com/doc/current/cookbook/profiler/profiling_data.html
https://symfony.com/blog/new-in-symfony-2-4-quicker-access-to-the-profiler-when-working-on-an-api
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XDebugTokenScanRule.java
