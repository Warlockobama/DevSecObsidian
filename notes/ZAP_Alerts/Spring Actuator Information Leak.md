
# Spring Actuator Information Leak

**ID:** 40042
**Risk Level:** Not specified
**CWE ID:** 215
**WASC ID:** 13
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Spring Actuator Information Leak"
alertid: 40042
alertindex: 4004200
alerttype: "Active"
alertcount: 1
status: release
type: alert
risk: Medium
solution: "Disable the Health Actuators and other actuators, or restrict them to administrative users."
references:
   - https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#overview
other: ""
cwe: 215
wasc: 13
techtags: 
  - Language.Java
  - Language.Java.Spring
alerttags: 
  - OWASP_2017_A05
  - OWASP_2021_A01
  - WSTG-v42-CONF-05
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SpringActuatorScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrules/SpringActuatorScanRule.java"
---
Spring Actuator for Health is enabled and may reveal sensitive information about this application. Spring Actuators can be used for real monitoring purposes, but should be used with caution as to not expose too much information about the application or the infrastructure running it.


## Solution
No solution provided.

## References
No references provided.
