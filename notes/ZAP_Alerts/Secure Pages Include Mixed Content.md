
# Secure Pages Include Mixed Content

**ID:** 10040
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Secure Pages Include Mixed Content"
alertid: 10040
alertindex: 1004000
alerttype: "Passive"
alertcount: 1
status: release
type: alert
solution: "A page that is available over SSL/TLS must be comprised completely of content which is transmitted over SSL/TLS. The page must not contain any content that is transmitted over unencrypted HTTP.  This includes content from third party sites."
references:
   - https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
other: ""
cwe: 311
wasc: 4
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-CRYP-03
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/MixedContentScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/MixedContentScanRule.java"
---
The page includes mixed content, that is content accessed via HTTP instead of HTTPS.


## Solution
No solution provided.

## References
No references provided.
