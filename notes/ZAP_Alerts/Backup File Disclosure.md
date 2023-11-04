
# Backup File Disclosure

**ID:** 10095
**Risk Level:** Not specified
**CWE ID:** 530
**WASC ID:** 34
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Backup File Disclosure"
alertid: 10095
alertindex: 1009500
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: "Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.  Consider using MVC based frameworks such as Struts."
references:
   - https://cwe.mitre.org/data/definitions/530.html
   - https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information.html
other: ""
cwe: 530
wasc: 34
alerttags: 
  - OWASP_2017_A03
  - OWASP_2021_A05
  - WSTG-v42-CONF-04
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/BackupFileDisclosureScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/BackupFileDisclosureScanRule.java"
---
A backup of the file was disclosed by the web server


## Solution
No solution provided.

## References
No references provided.
