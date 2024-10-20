
# User Controllable Charset

**ID:** 10030
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
This check looks at user-supplied input in query string parameters and POST data to identify where Content-Type or meta tag charset declarations might be user-controlled. Such charset declarations should always be declared by the application. If an attacker can control the response charset, they could manipulate the HTML to perform XSS or other attacks. For example, an attacker controlling the <meta> element charset value is able to declare UTF-7 and is also able to include enough user-controlled payload early in the HTML document to have it interpreted as UTF-7. By encoding their payload with UTF-7 the attacker is able to bypass any server-side XSS protections and embed script in the page.

## Solution
Force UTF-8 in all charset declarations. If user-input is required to decide a charset declaration, ensure that only an allowed list is used.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledCharsetScanRule.java
