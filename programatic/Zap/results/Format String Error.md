
# Format String Error

**ID:** 30002
**Risk Level:** Medium
**CWE ID:** 134
**WASC ID:** 6
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
A Format String error occurs when the submitted data of an input string is evaluated as a command by the application.

## Solution
Rewrite the background program using proper deletion of bad character strings.  This will require a recompile of the background executable.

## References
https://owasp.org/www-community/attacks/Format_string_attack
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/FormatStringScanRule.java
