
# Source Code Disclosure - WEB-INF folder

**ID:** 10045
**Risk Level:** Not specified
**CWE ID:** 541
**WASC ID:** 34
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Source Code Disclosure - /WEB-INF folder"
alertid: 10045
alertindex: 1004500
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: High
solution: "Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.  Consider using MVC based frameworks such as Struts."
references:
   - http://projects.webappsec.org/Predictable-Resource-Location
   - https://cwe.mitre.org/data/definitions/425.html
other: ""
cwe: 541
wasc: 34
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-CONF-05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SourceCodeDisclosureWebInfScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/SourceCodeDisclosureWebInfScanRule.java"
---
Predictable Resource Location is an attack technique used to uncover hidden web site content and functionality. By making educated guesses via brute forcing an attacker can guess file and directory names not intended for public viewing. Brute forcing filenames is easy because files/paths often have common naming convention and reside in standard locations. These can include temporary files, backup files, logs, administrative site sections, configuration files, demo applications, and sample files. These files may disclose sensitive information about the website, web application internals, database information, passwords, machine names, file paths to other sensitive areas, etc...

This will not only assist with identifying site surface which may lead to additional site vulnerabilities, but also may disclose valuable information to an attacker about the environment or its users. Predictable Resource Location is also known as Forced Browsing, Forceful Browsing, File Enumeration, and Directory Enumeration.


## Solution
No solution provided.

## References
No references provided.
