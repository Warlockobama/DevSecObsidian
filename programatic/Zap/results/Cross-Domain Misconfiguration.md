
# Cross-Domain Misconfiguration

**ID:** 10098
**Risk Level:** Medium
**CWE ID:** 264
**WASC ID:** 14
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server

## Solution
Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance). Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

## References
https://vulncat.fortify.com/en/detail?id=desc.config.dotnet.html5_overly_permissive_cors_policy
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CrossDomainMisconfigurationScanRule.java
