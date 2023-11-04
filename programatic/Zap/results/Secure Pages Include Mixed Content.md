
# Secure Pages Include Mixed Content

**ID:** 10040
**Risk Level:** Not specified
**CWE ID:** 311
**WASC ID:** 4
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The page includes mixed content, that is content accessed via HTTP instead of HTTPS.

## Solution
A page that is available over SSL/TLS must be comprised completely of content which is transmitted over SSL/TLS. The page must not contain any content that is transmitted over unencrypted HTTP.  This includes content from third party sites.

## References
https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/MixedContentScanRule.java
