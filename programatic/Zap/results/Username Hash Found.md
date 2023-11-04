
# Username Hash Found

**ID:** 10057
**Risk Level:** Informational
**CWE ID:** 284
**WASC ID:** 2
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A hash of a username (admin) was found in the response. This may indicate that the application is subject to an Insecure Direct Object Reference (IDOR) vulnerability. Manual testing will be required to see if this discovery can be abused.

## Solution
Use per user or session indirect object references (create a temporary mapping at time of use). Or, ensure that each use of a direct object reference is tied to an authorization check to ensure the user is authorized for the requested object. 

## References
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UsernameIdorScanRule.java
