
# X-AspNet-Version Response Header

**ID:** 10061
**Risk Level:** Low
**CWE ID:** 933
**WASC ID:** 14
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
Server leaks information via "X-AspNet-Version"/"X-AspNetMvc-Version" HTTP response header field(s).

## Solution
Configure the server so it will not return those headers.

## References
https://www.troyhunt.com/shhh-dont-let-your-response-headers/
https://blogs.msdn.microsoft.com/varunm/2013/04/23/remove-unwanted-http-response-headers/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XAspNetVersionScanRule.java
