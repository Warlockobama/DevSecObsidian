
# Bypassing 403

**ID:** 40038
**Risk Level:** Medium
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Bypassing 403 endpoints may be possible, the scan rule sent a payload that caused the response to be accessible (status code 200).

## Solution


## References
https://www.acunetix.com/blog/articles/a-fresh-look-on-reverse-proxy-related-attacks/
https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf
https://www.contextis.com/en/blog/server-technologies-reverse-proxy-bypass
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ForbiddenBypassScanRule.java
