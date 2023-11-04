
# Content Cacheability

**ID:** 10049
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Content Cacheability"
alertid: 10049
alertindex: 1004900
alerttype: "Passive"
status: beta
type: alertset
alerts:
   10049-1:
      alertid: 10049-1
      name: "Non-Storable Content"
   10049-2:
      alertid: 10049-2
      name: "Storable but Non-Cacheable Content"
   10049-3:
      alertid: 10049-3
      name: "Storable and Cacheable Content"
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/CacheableScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrulesBeta/CacheableScanRule.java"
---


## Solution
No solution provided.

## References
No references provided.
