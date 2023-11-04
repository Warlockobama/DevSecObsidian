
# Server Side Include

**ID:** 40009
**Risk Level:** Not specified
**CWE ID:** 97
**WASC ID:** 31
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Server Side Include"
alertid: 40009
alertindex: 4000900
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: High
solution: "Do not trust client side input and enforce a tight check in the server side. Disable server side includes. Refer to manual to disable Sever Side Include. Use least privilege to run your web server or application server. For Apache, disable the following: Options Indexes FollowSymLinks Includes AddType application/x-httpd-cgi .cgi AddType text/x-server-parsed-html .html"
references:
   - http://www.carleton.ca/~dmcfet/html/ssi.html
other: ""
cwe: 97
wasc: 31
techtags: 
  - OS.Linux
  - OS.MacOS
  - OS.Windows
alerttags: 
  - OWASP_2017_A01
  - OWASP_2021_A03
  - WSTG-v42-INPV-11
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ServerSideIncludeScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/ServerSideIncludeScanRule.java"
---
Certain parameters may cause Server Side Include commands to be executed.  This may allow database connection or arbitrary code to be executed.


## Solution
No solution provided.

## References
No references provided.
