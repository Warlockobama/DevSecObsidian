
# Insecure JSF ViewState

**ID:** 90001
**Risk Level:** Medium
**CWE ID:** 642
**WASC ID:** 14
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The response at the following URL contains a ViewState value that has no cryptographic protections.

## Solution
Secure VIEWSTATE with a MAC specific to your environment

## References
https://www.trustwave.com/spiderlabs/advisories/TWSL2010-001.txt
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureJsfViewStatePassiveScanRule.java
