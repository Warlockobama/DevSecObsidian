
# Expression Language Injection

**ID:** 90025
**Risk Level:** High
**CWE ID:** 917
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The software constructs all or part of an expression language (EL) statement in a Java Server Page (JSP) using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended EL statement before it is executed. In certain versions of Spring 3.0.5 and earlier, there was a vulnerability (CVE-2011-2730) in which Expression Language tags would be evaluated twice, which effectively exposed any application to EL injection. However, even for later versions, this weakness is still possible depending on configuration.

## Solution
Perform data validation best practice against untrusted input and to ensure that output encoding is applied when data arrives on the EL layer, so that no metacharacter is found by the interpreter within the user content before evaluation. The most obvious patterns to detect include ${ and #{, but it may be possible to encode or fragment this data.

## References
https://owasp.org/www-community/vulnerabilities/Expression_Language_Injection
http://cwe.mitre.org/data/definitions/917.html
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ExpressionLanguageInjectionScanRule.java
