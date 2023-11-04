
# Remote Code Execution - Shell Shock

**ID:** 10048
**Risk Level:** High
**CWE ID:** 78
**WASC ID:** 31
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The server is running a version of the Bash shell that allows remote attackers to execute arbitrary code

## Solution
Update Bash on the server to the latest version

## References
http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271
http://www.troyhunt.com/2014/09/everything-you-need-to-know-about.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ShellShockScanRule.java
