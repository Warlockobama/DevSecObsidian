
# User Agent Fuzzer

**ID:** 10104
**Risk Level:** Not specified
**CWE ID:** 0
**WASC ID:** 0
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "User Agent Fuzzer"
alertid: 10104
alertindex: 1010400
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Informational
solution: ""
references:
   - https://owasp.org/wstg
other: ""
alerttags: 
  - CUSTOM_PAYLOADS
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/UserAgentScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/UserAgentScanRule.java"
---
Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.


## Solution
No solution provided.

## References
No references provided.
