
# HTTP Server Response Header

**ID:** 10036
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "HTTP Server Response Header"
alertid: 10036
alertindex: 1003600
alerttype: "Passive"
status: release
type: alertset
alerts:
   10036-1:
      alertid: 10036-1
      name: "Server Leaks its Webserver Application via \"Server\" HTTP Response Header Field"
   10036-2:
      alertid: 10036-2
      name: "Server Leaks Version Information via \"Server\" HTTP Response Header Field"
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java"
---


## Solution
No solution provided.

## References
No references provided.
