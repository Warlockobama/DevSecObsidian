
# Bypassing 403

**ID:** 40038
**Risk Level:** Not specified
**CWE ID:** 0
**WASC ID:** 0
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Bypassing 403"
alertid: 40038
alertindex: 4003800
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: ""
references:
   - https://www.acunetix.com/blog/articles/a-fresh-look-on-reverse-proxy-related-attacks/
   - https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf
   - https://www.contextis.com/en/blog/server-technologies-reverse-proxy-bypass
other: ""
alerttags: 
  - OWASP_2017_A05
  - OWASP_2021_A01
  - WSTG-v42-ATHN-04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ForbiddenBypassScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/ForbiddenBypassScanRule.java"
---
Bypassing 403 endpoints may be possible, the scan rule sent a payload that caused the response to be accessible (status code 200).


## Solution
No solution provided.

## References
No references provided.
