
# Trace.axd Information Leak

**ID:** 40029
**Risk Level:** Medium
**CWE ID:** 215
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The ASP.NET Trace Viewer (trace.axd) was found to be available. This component can leak a significant amount of valuable information.

## Solution
Consider whether or not Trace Viewer is actually required in production, if it isn't then disable it. If it is then ensure access to it requires authentication and authorization.

## References
https://msdn.microsoft.com/en-us/library/bb386420.aspx
https://msdn.microsoft.com/en-us/library/wwh16c6c.aspx
https://www.dotnetperls.com/trace
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/TraceAxdScanRule.java
