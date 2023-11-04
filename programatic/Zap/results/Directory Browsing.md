
# Directory Browsing

**ID:** 10033
**Risk Level:** Medium
**CWE ID:** 548
**WASC ID:** 16
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
It is possible to view a listing of the directory contents. Directory listings may reveal hidden scripts, include files, backup source files, etc., which can be accessed to reveal sensitive information.

## Solution
Configure the web server to disable directory browsing.

## References
https://cwe.mitre.org/data/definitions/548.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/DirectoryBrowsingScanRule.java
