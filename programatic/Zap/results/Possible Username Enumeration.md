
# Possible Username Enumeration

**ID:** 40023
**Risk Level:** Informational
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
It may be possible to enumerate usernames, based on differing HTTP responses when valid and invalid usernames are provided. This would greatly increase the probability of success of password brute-forcing attacks against the system. Note that false positives may sometimes be minimised by increasing the 'Attack Strength' Option in ZAP.  Please manually check the 'Other Info' field to confirm if this is actually an issue.

## Solution
Do not divulge details of whether a username is valid or invalid. In particular, for unsuccessful login attempts, do not differentiate between an invalid user and an invalid password in the error message, page title, page contents, HTTP headers, or redirection logic.

## References
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account.html
http://sebastian-schinzel.de/_download/ifip-sec2011.pdf
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/UsernameEnumerationScanRule.java
