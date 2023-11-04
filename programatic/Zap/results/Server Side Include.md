
# Server Side Include

**ID:** 40009
**Risk Level:** High
**CWE ID:** 97
**WASC ID:** 31
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Certain parameters may cause Server Side Include commands to be executed.  This may allow database connection or arbitrary code to be executed.

## Solution
Do not trust client side input and enforce a tight check in the server side. Disable server side includes. Refer to manual to disable Sever Side Include. Use least privilege to run your web server or application server. For Apache, disable the following: Options Indexes FollowSymLinks Includes AddType application/x-httpd-cgi .cgi AddType text/x-server-parsed-html .html

## References
http://www.carleton.ca/~dmcfet/html/ssi.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ServerSideIncludeScanRule.java
