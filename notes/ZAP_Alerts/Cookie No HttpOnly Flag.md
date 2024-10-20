
# Cookie No HttpOnly Flag

**ID:** 10010
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Cookie No HttpOnly Flag"
alertid: 10010
alertindex: 1001000
alerttype: "Passive"
alertcount: 1
status: release
type: alert
risk: Low
solution: "Ensure that the HttpOnly flag is set for all cookies."
references:
   - https://owasp.org/www-community/HttpOnly
other: ""
cwe: 1004
wasc: 13
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-SESS-02
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieHttpOnlyScanRule.java
linktext: "org/zaproxy/zap/extension/pscanrules/CookieHttpOnlyScanRule.java"
---
A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.


## Solution
No solution provided.

## References
No references provided.
