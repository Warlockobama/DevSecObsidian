
# Reverse Tabnabbing

**ID:** 10108
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Reverse Tabnabbing"
alertid: 10108
alertindex: 1010800
alerttype: "Passive"
alertcount: 1
status: release
type: alert
solution: "Do not use a target attribute, or if you have to then also add the attribute: rel=\"noopener noreferrer\"."
references:
   - https://owasp.org/www-community/attacks/Reverse_Tabnabbing
   - https://dev.to/ben/the-targetblank-vulnerability-by-example
   - https://mathiasbynens.github.io/rel-noopener/
   - https://medium.com/@jitbit/target-blank-the-most-underestimated-vulnerability-ever-96e328301f4c
other: ""
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/LinkTargetScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/LinkTargetScanRule.java"
---
At least one link on this page is vulnerable to Reverse tabnabbing as it uses a target attribute without using both of the "noopener" and "noreferrer" keywords in the "rel" attribute, which allows the target page to take control of this page.


## Solution
No solution provided.

## References
No references provided.
