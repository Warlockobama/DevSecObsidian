
# Trace.axd Information Leak

**ID:** 40029
**Risk Level:** Not specified
**CWE ID:** 215
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Trace.axd Information Leak"
alertid: 40029
alertindex: 4002900
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Consider whether or not Trace Viewer is actually required in production, if it isn't then disable it. If it is then ensure access to it requires authentication and authorization."
references:
   - https://msdn.microsoft.com/en-us/library/bb386420.aspx
   - https://msdn.microsoft.com/en-us/library/wwh16c6c.aspx
   - https://www.dotnetperls.com/trace
other: ""
cwe: 215
wasc: 13
techtags: 
  - Db.Microsoft_SQL_Server
  - Language.ASP
  - OS.Windows
  - WS.IIS
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-CONF-05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/TraceAxdScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/TraceAxdScanRule.java"
---
The ASP.NET Trace Viewer (trace.axd) was found to be available. This component can leak a significant amount of valuable information.


## Solution
No solution provided.

## References
No references provided.
