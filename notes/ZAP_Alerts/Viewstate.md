
# Viewstate

**ID:** 10032
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Viewstate"
alertid: 10032
alertindex: 1003200
alerttype: "Passive"
status: release
type: alertset
alerts:
   10032-1:
      alertid: 10032-1
      name: "Potential IP Addresses Found in the Viewstate"
   10032-2:
      alertid: 10032-2
      name: "Emails Found in the Viewstate"
   10032-3:
      alertid: 10032-3
      name: "Old Asp.Net Version in Use"
   10032-4:
      alertid: 10032-4
      name: "Viewstate without MAC Signature (Unsure)"
   10032-5:
      alertid: 10032-5
      name: "Viewstate without MAC Signature (Sure)"
   10032-6:
      alertid: 10032-6
      name: "Split Viewstate in Use"
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ViewstateScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/ViewstateScanRule.java"
---


## Solution
No solution provided.

## References
No references provided.
