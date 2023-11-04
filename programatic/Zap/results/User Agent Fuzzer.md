
# User Agent Fuzzer

**ID:** 10104
**Risk Level:** Informational
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

## Solution


## References
https://owasp.org/wstg
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/UserAgentScanRule.java
