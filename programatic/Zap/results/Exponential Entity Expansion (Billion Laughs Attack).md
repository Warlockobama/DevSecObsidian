
# Exponential Entity Expansion (Billion Laughs Attack)

**ID:** 40044
**Risk Level:** Medium
**CWE ID:** 776
**WASC ID:** 44
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
An exponential entity expansion, or "billion laughs" attack is a type of denial-of-service (DoS) attack. It is aimed at parsers of markup languages like XML or YAML that allow macro expansions.

## Solution
Defenses against this kind of attack include capping the memory allocated in an individual parser if loss of the document is acceptable, or treating entities symbolically and expanding them lazily only when (and to the extent) their content is to be used.

## References
https://en.wikipedia.org/wiki/Billion_laughs_attack
http://projects.webappsec.org/XML-Entity-Expansion
http://cwe.mitre.org/data/definitions/776.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ExponentialEntityExpansionScanRule.java
