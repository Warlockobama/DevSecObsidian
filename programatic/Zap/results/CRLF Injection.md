
# CRLF Injection

**ID:** 40003
**Risk Level:** Medium
**CWE ID:** 113
**WASC ID:** 25
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Cookie can be set via CRLF injection.  It may also be possible to set arbitrary HTTP response headers. In addition, by carefully crafting the injected response using cross-site script, cache poisoning vulnerability may also exist.

## Solution
Type check the submitted parameter carefully.  Do not allow CRLF to be injected by filtering CRLF.

## References
http://www.watchfire.com/resources/HTTPResponseSplitting.pdf
http://webappfirewall.com/lib/crlf-injection.txtnull
http://www.securityfocus.com/bid/9804
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrlfInjectionScanRule.java
