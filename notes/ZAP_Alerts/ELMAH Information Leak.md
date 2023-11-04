
# ELMAH Information Leak

**ID:** 40028
**Risk Level:** Not specified
**CWE ID:** 94
**WASC ID:** 14
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "ELMAH Information Leak"
alertid: 40028
alertindex: 4002800
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Consider whether or not ELMAH is actually required in production, if it isn't then disable it. If it is then ensure access to it requires authentication and authorization. See also: https://elmah.github.io/a/securing-error-log-pages/"
references:
   - https://www.troyhunt.com/aspnet-session-hijacking-with-google/
   - https://www.nuget.org/packages/elmah
   - https://elmah.github.io/
other: ""
cwe: 94
wasc: 14
techtags: 
  - Db.Microsoft_SQL_Server
  - Language.ASP
  - OS.Windows
  - WS.IIS
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-CONF-05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ElmahScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/ElmahScanRule.java"
---
The Error Logging Modules and Handlers (ELMAH [elmah.axd]) HTTP Module was found to be available. This module can leak a significant amount of valuable information.


## Solution
No solution provided.

## References
No references provided.
