
# In Page Banner Information Leak

**ID:** 10009
**Risk Level:** Low
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The server returned a version banner string in the response content. Such information leaks may allow attackers to further target specific issues impacting the product and version in use.

## Solution
Configure the server to prevent such information leaks. For example: Under Tomcat this is done via the "server" directive and implementation of custom error pages. Under Apache this is done via the "ServerSignature" and "ServerTokens" directives.

## References
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/InPageBannerInfoLeakScanRule.java
