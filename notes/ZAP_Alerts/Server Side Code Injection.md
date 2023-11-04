
# Server Side Code Injection

**ID:** 90019
**Risk Level:** Not specified
**CWE ID:** 94
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Server Side Code Injection"
alertid: 90019
alertindex: 9001900
alerttype: "Active"
status: release
type: alertset
alerts:
   90019-1:
      alertid: 90019-1
      name: "Server Side Code Injection - PHP Code Injection"
   90019-2:
      alertid: 90019-2
      name: "Server Side Code Injection - ASP Code Injection"
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CodeInjectionScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/CodeInjectionScanRule.java"
---


## Solution
No solution provided.

## References
No references provided.
