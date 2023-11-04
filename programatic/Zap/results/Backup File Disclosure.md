
# Backup File Disclosure

**ID:** 10095
**Risk Level:** Medium
**CWE ID:** 530
**WASC ID:** 34
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
A backup of the file was disclosed by the web server

## Solution
Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.  Consider using MVC based frameworks such as Struts.

## References
https://cwe.mitre.org/data/definitions/530.html
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/BackupFileDisclosureScanRule.java
