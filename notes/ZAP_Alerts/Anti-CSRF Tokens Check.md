
# Anti-CSRF Tokens Check

**ID:** 20012
**Risk Level:** Not specified
**CWE ID:** 352
**WASC ID:** 9
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Anti-CSRF Tokens Check"
alertid: 20012
alertindex: 2001200
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: "Phase: Architecture and Design Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, use anti-CSRF packages such as the OWASP CSRFGuard.  Phase: Implementation Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.  Phase: Architecture and Design Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330). Note that this can be bypassed using XSS.  Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation. Note that this can be bypassed using XSS.  Use the ESAPI Session Management control. This control includes a component for CSRF.  Do not use the GET method for any request that triggers a state change.  Phase: Implementation Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons."
references:
   - http://projects.webappsec.org/Cross-Site-Request-Forgery
   - https://cwe.mitre.org/data/definitions/352.html
other: ""
cwe: 352
wasc: 9
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-SESS-05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/CsrfTokenScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/CsrfTokenScanRule.java"
---
A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.


## Solution
No solution provided.

## References
No references provided.
