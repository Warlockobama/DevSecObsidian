
# Insecure HTTP Method

**ID:** 90028
**Risk Level:** Not specified
**CWE ID:** 200
**WASC ID:** 45
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
---
title: "Insecure HTTP Method"
alertid: 90028
alertindex: 9002800
alerttype: "Active"
alertcount: 1
status: beta
type: alert
risk: Medium
solution: ""
references:
   - http://projects.webappsec.org/Fingerprinting
other: ""
cwe: 200
wasc: 45
alerttags: 
  - OWASP_2017_A06
  - OWASP_2021_A05
  - WSTG-v42-CONF-06
code: https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java
linktext: "org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java"
---
The most common methodology for attackers is to first footprint the target's web presence and enumerate as much information as possible. With this information, the attacker may develop an accurate attack scenario, which will effectively exploit a vulnerability in the software type/version being utilized by the target host.

Multi-tier fingerprinting is similar to its predecessor, TCP/IP Fingerprinting (with a scanner such as Nmap) except that it is focused on the Application Layer of the OSI model instead of the Transport Layer. The theory behind this fingerprinting is to create an accurate profile of the target's platform, web application software technology, backend database version, configurations and possibly even their network architecture/topology.


## Solution
No solution provided.

## References
No references provided.
