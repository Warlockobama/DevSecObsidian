
# Insecure HTTP Method

**ID:** 90028
**Risk Level:** Medium
**CWE ID:** 200
**WASC ID:** 45
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The most common methodology for attackers is to first footprint the target's web presence and enumerate as much information as possible. With this information, the attacker may develop an accurate attack scenario, which will effectively exploit a vulnerability in the software type/version being utilized by the target host.

Multi-tier fingerprinting is similar to its predecessor, TCP/IP Fingerprinting (with a scanner such as Nmap) except that it is focused on the Application Layer of the OSI model instead of the Transport Layer. The theory behind this fingerprinting is to create an accurate profile of the target's platform, web application software technology, backend database version, configurations and possibly even their network architecture/topology.

## Solution


## References
http://projects.webappsec.org/Fingerprinting
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java
