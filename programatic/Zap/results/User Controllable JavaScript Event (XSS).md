
# User Controllable JavaScript Event (XSS)

**ID:** 10043
**Risk Level:** Not specified
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

## Solution
Validate all input and sanitize output it before writing to any Javascript on* events.

## References
http://websecuritytool.codeplex.com/wikipage?title=Checks#user-javascript-event
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledJavascriptEventScanRule.java
