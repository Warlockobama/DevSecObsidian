
# Private IP Disclosure

**ID:** 2
**Risk Level:** Low
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
A private IP (such as 10.x.x.x, 172.x.x.x, 192.168.x.x) or an Amazon EC2 private hostname (for example, ip-10-0-56-78) has been found in the HTTP response body. This information might be helpful for further attacks targeting internal systems.

## Solution
Remove the private IP address from the HTTP response body.  For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

## References
https://tools.ietf.org/html/rfc1918
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoPrivateAddressDisclosureScanRule.java
