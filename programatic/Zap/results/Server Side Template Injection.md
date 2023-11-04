
# Server Side Template Injection

**ID:** 90035
**Risk Level:** High
**CWE ID:** 94
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
When the user input is inserted in the template instead of being used as argument in rendering is evaluated by the template engine. Depending on the template engine it can lead to remote code execution.

## Solution
Instead of inserting the user input in the template, use it as rendering argument.

## References
https://portswigger.net/blog/server-side-template-injection
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SstiScanRule.java
