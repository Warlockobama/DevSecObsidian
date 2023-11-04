
# Information Disclosure - Sensitive Information in URL

**ID:** 10024
**Risk Level:** Informational
**CWE ID:** 200
**WASC ID:** 13
**Attack Strength:** Not specified
**Alert Threshold:** DEFAULT

## Rule Description
The request appeared to contain sensitive information leaked in the URL. This can violate PCI and most organizational compliance policies. You can configure the list of strings for this check to add or remove values specific to your environment.

## Solution
Do not pass sensitive information in URIs.

## References
https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InformationDisclosureInUrlScanRule.java
