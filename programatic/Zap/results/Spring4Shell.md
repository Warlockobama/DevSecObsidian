
# Spring4Shell

**ID:** 40045
**Risk Level:** High
**CWE ID:** 78
**WASC ID:** 20
**Attack Strength:** DEFAULT
**Alert Threshold:** DEFAULT

## Rule Description
The application appears to be vulnerable to CVE-2022-22965 (otherwise known as Spring4Shell) - remote code execution (RCE) via data binding.

## Solution
Upgrade Spring Framework to versions 5.3.18, 5.2.20, or newer.

## References
https://nvd.nist.gov/vuln/detail/CVE-2022-22965
https://www.rapid7.com/blog/post/2022/03/30/spring4shell-zero-day-vulnerability-in-spring-framework/
https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement#vulnerability
https://tanzu.vmware.com/security/cve-2022-22965
https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/Spring4ShellScanRule.java
