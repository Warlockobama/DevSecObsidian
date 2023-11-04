
# XML External Entity Attack

**ID:** 90023
**Risk Level:** High
**CWE ID:** 611
**WASC ID:** 43
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
This technique takes advantage of a feature of XML to build documents dynamically at the time of processing. An XML message can either provide data explicitly or by pointing to an URI where the data exists. In the attack technique, external entities may replace the entity value with malicious data, alternate referrals or may compromise the security of the data the server/XML application has access to.
	Attackers may also use External Entities to have the web services server download malicious code or content to the server for use in secondary or follow on attacks.

## Solution


## References
http://projects.webappsec.org/XML-External-Entities
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/XxeScanRule.java
