
# XSLT Injection

**ID:** 90017
**Risk Level:** Medium
**CWE ID:** 91
**WASC ID:** 23
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Injection using XSL transformations may be possible, and may allow an attacker to read system information, read and write files, or execute arbitrary code.

## Solution
Sanitize and analyze every user input coming from any client-side.

## References
https://www.contextis.com/blog/xslt-server-side-injection-attacks
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/XsltInjectionScanRule.java
