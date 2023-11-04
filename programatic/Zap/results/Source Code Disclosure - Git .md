
# Source Code Disclosure - Git 

**ID:** 41
**Risk Level:** High
**CWE ID:** 541
**WASC ID:** 34
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The source code for the current page was disclosed by the web server.

## Solution
Ensure that Git metadata files are not deployed to the web server or application server

## References
http://projects.webappsec.org/Predictable-Resource-Location
https://cwe.mitre.org/data/definitions/425.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/SourceCodeDisclosureGitScanRule.java
