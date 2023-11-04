
# Source Code Disclosure - PHP

**ID:** 10099
**Risk Level:** Medium
**CWE ID:** 540
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
Application Source Code was disclosed by the web server - PHP

## Solution
Ensure that application Source Code is not available with alternative extensions, and ensure that source code is not present within other files or data deployed to the web server, or served by the web server. 

## References
https://www.wsj.com/articles/BL-CIOB-2999
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/SourceCodeDisclosureScanRule.java
