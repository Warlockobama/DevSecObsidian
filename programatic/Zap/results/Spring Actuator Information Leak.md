
# Spring Actuator Information Leak

**ID:** 40042
**Risk Level:** Medium
**CWE ID:** 215
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
Spring Actuator for Health is enabled and may reveal sensitive information about this application. Spring Actuators can be used for real monitoring purposes, but should be used with caution as to not expose too much information about the application or the infrastructure running it.

## Solution
Disable the Health Actuators and other actuators, or restrict them to administrative users.

## References
https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#overview
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SpringActuatorScanRule.java
