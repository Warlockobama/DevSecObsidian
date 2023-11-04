
# Integer Overflow Error

**ID:** 30003
**Risk Level:** Medium
**CWE ID:** 190
**WASC ID:** 3
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
An integer overflow condition exists when an integer used in a compiled program extends beyond the range limits and has not been properly checked from the input stream.

## Solution
In order to prevent overflows and divide by 0 (zero) errors in the application, please rewrite the backend program, checking if the values of integers being processed are within the application's allowed range. This will require a recompilation of the backend executable.

## References
https://en.wikipedia.org/wiki/Integer_overflow
https://cwe.mitre.org/data/definitions/190.html
http://projects.webappsec.org/w/page/13246946/Integer%20Overflows
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/IntegerOverflowScanRule.java
