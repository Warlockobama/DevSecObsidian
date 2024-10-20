
# Cookie Without Secure Flag

**ID:** 10011
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Cookie Without Secure Flag"
alertid: 10011
alertindex: 1001100
alerttype: "Passive"
alertcount: 1
status: release
type: alert
risk: Low
solution: "Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted channel. Ensure that the secure flag is set for cookies containing such sensitive information."
references:
   - https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html
other: ""
cwe: 614
wasc: 13
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-SESS-02
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieSecureFlagScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/CookieSecureFlagScanRule.java"
---
A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.


## Solution
No solution provided.

## References
No references provided.
