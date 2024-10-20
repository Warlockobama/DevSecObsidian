
# Cloud Metadata Potentially Exposed

**ID:** 90034
**Risk Level:** High
**CWE ID:** Not specified
**WASC ID:** Not specified
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The Cloud Metadata Attack attempts to abuse a misconfigured NGINX server in order to access the instance metadata maintained by cloud service providers such as AWS, GCP and Azure.
All of these providers provide metadata via an internal unroutable IP address '169.254.169.254' - this can be exposed by incorrectly configured NGINX servers and accessed by using this IP address in the Host header field.

## Solution
Do not trust any user data in NGINX configs. In this case it is probably the use of the $host variable which is set from the 'Host' header and can be controlled by an attacker.

## References
https://www.nginx.com/blog/trust-no-one-perils-of-trusting-user-input/
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CloudMetadataScanRule.java
