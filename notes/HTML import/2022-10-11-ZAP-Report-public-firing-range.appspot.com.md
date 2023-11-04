     

# ZAP Scanning Report

Generated with [![The ZAP logo](2022-10-11-ZAP-Report-public-firing-range.appspot.com/zap32x32.png)ZAP](https://zaproxy.org) on Tue 11 Oct 2022, at 19:08:16

## Contents

1. [About this report](#about-this-report)
    1. [Report parameters](#report-parameters)
- [Summaries](#summaries)
    1. [Alert counts by risk and confidence](#risk-confidence-counts)
    2. [Alert counts by site and risk](#site-risk-counts)
    3. [Alert counts by alert type](#alert-type-counts)
- [Alerts](#alerts)
    1. [Risk=High, Confidence=High (1)](#alerts--risk-3-confidence-3)
    2. [Risk=High, Confidence=Medium (2)](#alerts--risk-3-confidence-2)
    3. [Risk=Medium, Confidence=High (4)](#alerts--risk-2-confidence-3)
    4. [Risk=Medium, Confidence=Medium (5)](#alerts--risk-2-confidence-2)
    5. [Risk=Medium, Confidence=Low (1)](#alerts--risk-2-confidence-1)
    6. [Risk=Low, Confidence=Medium (6)](#alerts--risk-1-confidence-2)
    7. [Risk=Informational, Confidence=Low (2)](#alerts--risk-0-confidence-1)
- [Appendix](#appendix)
    1. [Alert types](#alert-types)

## About this report

### Report parameters

#### Contexts

The following contexts were selected to be included:

- public-firing-range.appspot.com

#### Sites

The following sites were included:

- https://public-firing-range.appspot.com

(If no sites were selected, all sites were included by default.)

An included site must also be within one of the included contexts for its data to be included in the report.

#### Risk levels

Included: High, Medium, Low, Informational

Excluded: None

#### Confidence levels

Included: User Confirmed, High, Medium, Low

Excluded: User Confirmed, High, Medium, Low, False Positive

## Summaries

### Alert counts by risk and confidence

This table shows the number of alerts for each level of risk and confidence included in the report.
(The percentages in brackets represent the count as a percentage of the total number of alerts included in the report, rounded to one decimal place.)
   
||   |Confidence|   |   |   |   |
|---|---|---|---|---|---|---|
|User Confirmed|High|Medium|Low|Total|
|---|---|---|---|---|
|Risk|High|0  <br>(0.0%)|1  <br>(4.8%)|2  <br>(9.5%)|0  <br>(0.0%)|3  <br>(14.3%)|
|Medium|0  <br>(0.0%)|4  <br>(19.0%)|5  <br>(23.8%)|1  <br>(4.8%)|10  <br>(47.6%)|
|Low|0  <br>(0.0%)|0  <br>(0.0%)|6  <br>(28.6%)|0  <br>(0.0%)|6  <br>(28.6%)|
|Informational|0  <br>(0.0%)|0  <br>(0.0%)|0  <br>(0.0%)|2  <br>(9.5%)|2  <br>(9.5%)|
|Total|0  <br>(0.0%)|5  <br>(23.8%)|13  <br>(61.9%)|3  <br>(14.3%)|21  <br>(100%)|

### Alert counts by site and risk

This table shows, for each site for which one or more alerts were raised, the number of alerts raised at each risk level.
Alerts with a confidence level of "False Positive" have been excluded from these counts.
(The numbers in brackets are the number of alerts raised for the site at or above that risk level.)
  
||   |Risk|   |   |   |
|---|---|---|---|---|---|
|High  <br>(= High)|Medium  <br>(>= Medium)|Low  <br>(>= Low)|Informational  <br>(>= Informational)|
|---|---|---|---|
|Site|https://public-firing-range.appspot.com|3  <br>(3)|10  <br>(13)|6  <br>(19)|2  <br>(21)|

### Alert counts by alert type

This table shows the number of alerts of each alert type, together with the alert type's risk level.
(The percentages in brackets represent each count as a percentage, rounded to one decimal place, of the total number of alerts included in this report.)
|Alert type|Risk|Count|
|---|---|---|
|[Cross Site Scripting (DOM Based)](#alert-type-0)|High|20  <br>(95.2%)|
|[Cross Site Scripting (Reflected)](#alert-type-1)|High|69  <br>(328.6%)|
|[External Redirect](#alert-type-2)|High|3  <br>(14.3%)|
|[.htaccess Information Leak](#alert-type-3)|Medium|6  <br>(28.6%)|
|[Absence of Anti-CSRF Tokens](#alert-type-4)|Medium|4  <br>(19.0%)|
|[CSP: Wildcard Directive](#alert-type-5)|Medium|6  <br>(28.6%)|
|[CSP: script-src unsafe-inline](#alert-type-6)|Medium|6  <br>(28.6%)|
|[CSP: style-src unsafe-inline](#alert-type-7)|Medium|6  <br>(28.6%)|
|[Content Security Policy (CSP) Header Not Set](#alert-type-8)|Medium|352  <br>(1,676.2%)|
|[Format String Error](#alert-type-9)|Medium|1  <br>(4.8%)|
|[Missing Anti-clickjacking Header](#alert-type-10)|Medium|303  <br>(1,442.9%)|
|[Secure Pages Include Mixed Content (Including Scripts)](#alert-type-11)|Medium|4  <br>(19.0%)|
|[X-Frame-Options Setting Malformed](#alert-type-12)|Medium|1  <br>(4.8%)|
|[Application Error Disclosure](#alert-type-13)|Low|11  <br>(52.4%)|
|[Cookie Without Secure Flag](#alert-type-14)|Low|2  <br>(9.5%)|
|[Cookie without SameSite Attribute](#alert-type-15)|Low|2  <br>(9.5%)|
|[Cross-Domain JavaScript Source File Inclusion](#alert-type-16)|Low|26  <br>(123.8%)|
|[Private IP Disclosure](#alert-type-17)|Low|1  <br>(4.8%)|
|[X-Content-Type-Options Header Missing](#alert-type-18)|Low|338  <br>(1,609.5%)|
|[Information Disclosure - Suspicious Comments](#alert-type-19)|Informational|6  <br>(28.6%)|
|[Re-examine Cache-control Directives](#alert-type-20)|Informational|25  <br>(119.0%)|
|Total||21|

## Alerts

1. ### Risk=High, Confidence=High (1)
    
    1. #### https://public-firing-range.appspot.com (1)
        
        1. ##### [Cross Site Scripting (DOM Based)](#alert-type-0) (1)
            
            1. POST https://public-firing-range.appspot.com/reflected/parameter/form#javascript:alert(5397)
                
                |   |   |
                |---|---|
                |Alert tags|- [WSTG-v42-CLNT-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting)<br>- [OWASP_2021_A03](https://owasp.org/Top10/A03_2021-Injection/)<br>- [OWASP_2017_A07](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS).html)|
                |Alert description|Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied code into a user's browser instance. A browser instance can be a standard web browser client, or a browser object embedded in a software product such as the browser within WinAmp, an RSS reader, or an email client. The code itself is usually written in HTML/JavaScript, but may also extend to VBScript, ActiveX, Java, Flash, or any other browser-supported technology.<br><br>When an attacker gets a user's browser to execute his/her code, the code will run within the security context (or zone) of the hosting web site. With this level of privilege, the code has the ability to read, modify and transmit any sensitive data accessible by the browser. A Cross-site Scripted user could have his/her account hijacked (cookie theft), their browser redirected to another location, or possibly shown fraudulent content delivered by the web site they are visiting. Cross-site Scripting attacks essentially compromise the trust relationship between a user and the web site. Applications utilizing browser object instances which load content from the file system may execute code under the local machine zone allowing for system compromise.<br><br>There are three types of Cross-site Scripting attacks: non-persistent, persistent and DOM-based.<br><br>Non-persistent attacks and DOM-based attacks require a user to either visit a specially crafted link laced with malicious code, or visit a malicious web page containing a web form, which when posted to the vulnerable site, will mount the attack. Using a malicious form will oftentimes take place when the vulnerable resource only accepts HTTP POST requests. In such a case, the form can be submitted automatically, without the victim's knowledge (e.g. by using JavaScript). Upon clicking on the malicious link or submitting the malicious form, the XSS payload will get echoed back and will get interpreted by the user's browser and execute. Another technique to send almost arbitrary requests (GET and POST) is by using an embedded client, such as Adobe Flash.<br><br>Persistent attacks occur when the malicious code is submitted to a web site where it's stored for a period of time. Examples of an attacker's favorite targets often include message board posts, web mail messages, and web chat software. The unsuspecting user is not required to interact with any additional site/link (e.g. an attacker site or a malicious link sent via email), just simply view the web page containing the code.|
                |Other info|Tag name: input Att name: q Att id:|
                |Request|Request line and header section (399 bytes)<br><br>```<br>POST https://public-firing-range.appspot.com/reflected/parameter/form HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Content-Type: application/x-www-form-urlencoded<br>Referer: https://public-firing-range.appspot.com/reflected/parameter/form<br>Content-Length: 5<br><br>```<br><br>Request body (5 bytes)<br><br>```<br>q=ZAP<br>```|
                |Response|Status line and header section (14 bytes)<br><br>```<br>HTTP/1.0 0<br><br>```<br><br>Response body (0 bytes)|
                |Attack|```<br>#javascript:alert(5397)<br>```|
                |Solution|Phase: Architecture and Design<br><br>Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.<br><br>Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.<br><br>Phases: Implementation; Architecture and Design<br><br>Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies.<br><br>For any data that will be output to another web page, especially any data that was received from external inputs, use the appropriate encoding on all non-alphanumeric characters.<br><br>Consult the XSS Prevention Cheat Sheet for more details on the types of encoding and escaping that are needed.<br><br>Phase: Architecture and Design<br><br>For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.<br><br>If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated.<br><br>Phase: Implementation<br><br>For every web page that is generated, use and specify a character encoding such as ISO-8859-1 or UTF-8. When an encoding is not specified, the web browser may choose a different encoding by guessing which encoding is actually being used by the web page. This can cause the web browser to treat certain sequences as special, opening up the client to subtle XSS attacks. See CWE-116 for more mitigations related to encoding/escaping.<br><br>To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XMLHTTPRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.<br><br>Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.<br><br>When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."<br><br>Ensure that you perform input validation at well-defined interfaces within the application. This will help protect the application even if a component is reused or moved elsewhere.|
                
2. ### Risk=High, Confidence=Medium (2)
    
    1. #### https://public-firing-range.appspot.com (2)
        
        1. ##### [Cross Site Scripting (Reflected)](#alert-type-1) (1)
            
            1. POST https://public-firing-range.appspot.com/reflected/parameter/form
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A03](https://owasp.org/Top10/A03_2021-Injection/)<br>- [WSTG-v42-INPV-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)<br>- [OWASP_2017_A07](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS).html)|
                |Alert description|Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied code into a user's browser instance. A browser instance can be a standard web browser client, or a browser object embedded in a software product such as the browser within WinAmp, an RSS reader, or an email client. The code itself is usually written in HTML/JavaScript, but may also extend to VBScript, ActiveX, Java, Flash, or any other browser-supported technology.<br><br>When an attacker gets a user's browser to execute his/her code, the code will run within the security context (or zone) of the hosting web site. With this level of privilege, the code has the ability to read, modify and transmit any sensitive data accessible by the browser. A Cross-site Scripted user could have his/her account hijacked (cookie theft), their browser redirected to another location, or possibly shown fraudulent content delivered by the web site they are visiting. Cross-site Scripting attacks essentially compromise the trust relationship between a user and the web site. Applications utilizing browser object instances which load content from the file system may execute code under the local machine zone allowing for system compromise.<br><br>There are three types of Cross-site Scripting attacks: non-persistent, persistent and DOM-based.<br><br>Non-persistent attacks and DOM-based attacks require a user to either visit a specially crafted link laced with malicious code, or visit a malicious web page containing a web form, which when posted to the vulnerable site, will mount the attack. Using a malicious form will oftentimes take place when the vulnerable resource only accepts HTTP POST requests. In such a case, the form can be submitted automatically, without the victim's knowledge (e.g. by using JavaScript). Upon clicking on the malicious link or submitting the malicious form, the XSS payload will get echoed back and will get interpreted by the user's browser and execute. Another technique to send almost arbitrary requests (GET and POST) is by using an embedded client, such as Adobe Flash.<br><br>Persistent attacks occur when the malicious code is submitted to a web site where it's stored for a period of time. Examples of an attacker's favorite targets often include message board posts, web mail messages, and web chat software. The unsuspecting user is not required to interact with any additional site/link (e.g. an attacker site or a malicious link sent via email), just simply view the web page containing the code.|
                |Request|Request line and header section (400 bytes)<br><br>```<br>POST https://public-firing-range.appspot.com/reflected/parameter/form HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Content-Type: application/x-www-form-urlencoded<br>Referer: https://public-firing-range.appspot.com/reflected/parameter/form<br>Content-Length: 61<br><br>```<br><br>Request body (61 bytes)<br><br>```<br>q=%3C%2Fp%3E%3CscrIpt%3Ealert%281%29%3B%3C%2FscRipt%3E%3Cp%3E<br>```|
                |Response|Status line and header section (502 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: ff0f1562d5459d0cf86b753b19754fe8<br>Date: Tue, 11 Oct 2022 19:36:14 GMT<br>Server: Google Frontend<br>Content-Length: 212<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (212 bytes)<br><br>```<br><html><br>  <body><br>    <p><br>      Previous submit: </p><scrIpt>alert(1);</scRipt><p><br>    </p><br>    <br>    <form method="POST"><br>      <input type="text" name="q"><br>      <input type="submit"><br>    </form><br>  </body><br></html><br>```|
                |Parameter|```<br>q<br>```|
                |Attack|```<br></p><scrIpt>alert(1);</scRipt><p><br>```|
                |Evidence|```<br></p><scrIpt>alert(1);</scRipt><p><br>```|
                |Solution|Phase: Architecture and Design<br><br>Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.<br><br>Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.<br><br>Phases: Implementation; Architecture and Design<br><br>Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies.<br><br>For any data that will be output to another web page, especially any data that was received from external inputs, use the appropriate encoding on all non-alphanumeric characters.<br><br>Consult the XSS Prevention Cheat Sheet for more details on the types of encoding and escaping that are needed.<br><br>Phase: Architecture and Design<br><br>For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.<br><br>If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated.<br><br>Phase: Implementation<br><br>For every web page that is generated, use and specify a character encoding such as ISO-8859-1 or UTF-8. When an encoding is not specified, the web browser may choose a different encoding by guessing which encoding is actually being used by the web page. This can cause the web browser to treat certain sequences as special, opening up the client to subtle XSS attacks. See CWE-116 for more mitigations related to encoding/escaping.<br><br>To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XMLHTTPRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.<br><br>Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.<br><br>When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."<br><br>Ensure that you perform input validation at well-defined interfaces within the application. This will help protect the application even if a component is reused or moved elsewhere.|
                
        2. ##### [External Redirect](#alert-type-2) (1)
            
            1. GET https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS?url=http%3A%2F%2F2187747390858742136.owasp.org
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A03](https://owasp.org/Top10/A03_2021-Injection/)<br>- [WSTG-v42-CLNT-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/04-Testing_for_Client-side_URL_Redirect)<br>- [OWASP_2017_A01](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html)|
                |Alert description|URL redirectors represent common functionality employed by web sites to forward an incoming request to an alternate resource. This can be done for a variety of reasons and is often done to allow resources to be moved within the directory structure and to avoid breaking functionality for users that request the resource at its previous location. URL redirectors may also be used to implement load balancing, leveraging abbreviated URLs or recording outgoing links. It is this last implementation which is often used in phishing attacks as described in the example below. URL redirectors do not necessarily represent a direct security vulnerability but can be abused by attackers trying to social engineer victims into believing that they are navigating to a site other than the true destination.|
                |Other info|The response contains a redirect in its Location header which allows an external Url to be set.|
                |Request|Request line and header section (400 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS?url=http%3A%2F%2F2187747390858742136.owasp.org HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/redirect/index.html<br>Content-Length: 0<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (406 bytes)<br><br>```<br>HTTP/1.1 302 Found<br>Location: http://2187747390858742136.owasp.org<br>X-Cloud-Trace-Context: e8822858437163855e40738c63d26804<br>Date: Tue, 11 Oct 2022 19:34:00 GMT<br>Content-Type: text/html<br>Server: Google Frontend<br>Content-Length: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (0 bytes)|
                |Parameter|```<br>url<br>```|
                |Attack|```<br>http://2187747390858742136.owasp.org<br>```|
                |Evidence|```<br>http://2187747390858742136.owasp.org<br>```|
                |Solution|Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.<br><br>When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."<br><br>Use an allow list of approved URLs or domains to be used for redirection.<br><br>Use an intermediate disclaimer page that provides the user with a clear warning that they are leaving your site. Implement a long timeout before the redirect occurs, or force the user to click on the link. Be careful to avoid XSS problems when generating the disclaimer page.<br><br>When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.<br><br>For example, ID 1 could map to "/login.asp" and ID 2 could map to "http://www.example.com/". Features such as the ESAPI AccessReferenceMap provide this capability.<br><br>Understand all the potential areas where untrusted inputs can enter your software: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.<br><br>Many open redirect problems occur because the programmer assumed that certain inputs could not be modified, such as cookies and hidden form fields.|
                
3. ### Risk=Medium, Confidence=High (4)
    
    1. #### https://public-firing-range.appspot.com (4)
        
        1. ##### [CSP: Wildcard Directive](#alert-type-5) (1)
            
            1. GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.|
                |Other info|The following directives either allow wildcard sources (or ancestors), are not defined, or are overly broadly defined:<br><br>script-src, style-src, img-src, connect-src, frame-src, font-src, media-src, object-src, manifest-src, worker-src, prefetch-src, form-action<br><br>The directive(s): form-action are among the directives that do not fallback to default-src, missing/excluding them is the same as allowing anything.|
                |Request|Request line and header section (359 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/invalidframingconfig/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (591 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Frame-Options: ALLOW-FROM https://example.com<br>Content-Security-Policy: frame-ancestors https://google.com<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: e85f2b8f8f1ce127681ef97e74036056<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 165<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (165 bytes)<br><br>```<br><!DOCTYPE html><br><title>Invalid framing configuration</title><br>X-Frame-Options ALLOW-FROM is set but the mentioned domain is not in the<br>CSP frame-ancestors definition.<br>```|
                |Parameter|```<br>Content-Security-Policy<br>```|
                |Evidence|```<br>frame-ancestors https://google.com<br>```|
                |Solution|Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.|
                
        2. ##### [CSP: script-src unsafe-inline](#alert-type-6) (1)
            
            1. GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.|
                |Other info|script-src includes unsafe-inline.|
                |Request|Request line and header section (359 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/invalidframingconfig/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (591 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Frame-Options: ALLOW-FROM https://example.com<br>Content-Security-Policy: frame-ancestors https://google.com<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: e85f2b8f8f1ce127681ef97e74036056<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 165<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (165 bytes)<br><br>```<br><!DOCTYPE html><br><title>Invalid framing configuration</title><br>X-Frame-Options ALLOW-FROM is set but the mentioned domain is not in the<br>CSP frame-ancestors definition.<br>```|
                |Parameter|```<br>Content-Security-Policy<br>```|
                |Evidence|```<br>frame-ancestors https://google.com<br>```|
                |Solution|Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.|
                
        3. ##### [CSP: style-src unsafe-inline](#alert-type-7) (1)
            
            1. GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.|
                |Other info|style-src includes unsafe-inline.|
                |Request|Request line and header section (359 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnocoverdomain HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/invalidframingconfig/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (591 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Frame-Options: ALLOW-FROM https://example.com<br>Content-Security-Policy: frame-ancestors https://google.com<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: e85f2b8f8f1ce127681ef97e74036056<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 165<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (165 bytes)<br><br>```<br><!DOCTYPE html><br><title>Invalid framing configuration</title><br>X-Frame-Options ALLOW-FROM is set but the mentioned domain is not in the<br>CSP frame-ancestors definition.<br>```|
                |Parameter|```<br>Content-Security-Policy<br>```|
                |Evidence|```<br>frame-ancestors https://google.com<br>```|
                |Solution|Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.|
                
        4. ##### [Content Security Policy (CSP) Header Not Set](#alert-type-8) (1)
            
            1. GET https://public-firing-range.appspot.com
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.|
                |Request|Request line and header section (230 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (458 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 074807e4900f2a8ee4825671b397ea7b<br>Server: Google Frontend<br>Content-Length: 1780<br>Date: Tue, 11 Oct 2022 19:01:10 GMT<br>Expires: Tue, 11 Oct 2022 19:11:10 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1780 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br><title>Firing Range</title><br></head><br><body><br>   <h1>Version 0.48</h1><br>   <h1>What is the Firing Range?</h1><br>   <p><br>     Firing Range is a test bed for automated web application security scanners. <br><br>     Its test cases are not meant<br>     to be hard to reach or exercise, as the site can be very easily crawlable. <br><br>     The testbed focuses on detection capabilities, presenting many variants of vulnerabilities and<br>     hard-to-detect edge cases.<br><br>     For more details, see the <a href="https://github.com/google/firing-range">GitHub page</a>.<br>  </p><br>  <ul><br>    <li><a href="/address/index.html">Address DOM XSS</a></li><br>    <li><a href="/angular/index.html">Angular-based XSSes</a></li><br>    <li><a href="/badscriptimport/index.html">Bad JavaScript imports</a></li><br>    <li><a href="/cors/index.html">CORS related vulnerabilities</a></li><br>    <li><a href="/dom/index.html">DOM XSS</a></li><br>    <li><a href="/escape/index.html">Escaped XSS</a></li><br>    <li><a href="/flashinjection/index.html">Flash Injection</a></li><br>    <li><a href="/mixedcontent/index.html">Mixed content</a></li><br>    <li><a href="/redirect/index.html">Redirect XSS</a></li><br>    <li><a href="/reflected/index.html">Reflected XSS</a></li><br>    <li><a href="/remoteinclude/index.html">Remote inclusion XSS</a></li><br>    <li><a href="/reverseclickjacking/">Reverse ClickJacking</a></li><br>    <li><a href="/tags/index.html">Tag based XSS</a></li><br>    <li><a href="/urldom/index.html">URL-based DOM XSS</a></li><br>    <li><a href="/vulnerablelibraries/index.html">Vulnerable libraries</a></li><br>    <li><a href="/leakedcookie/index.html">Leaked httpOnly cookie</a></li><br>    <li><a href="/invalidframingconfig/index.html">Invalid framing configuration</a></li><br>  </ul><br></body><br></html><br>```|
                |Solution|Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header, to achieve optimal browser support: "Content-Security-Policy" for Chrome 25+, Firefox 23+ and Safari 7+, "X-Content-Security-Policy" for Firefox 4.0+ and Internet Explorer 10+, and "X-WebKit-CSP" for Chrome 14+ and Safari 6+.|
                
4. ### Risk=Medium, Confidence=Medium (5)
    
    1. #### https://public-firing-range.appspot.com (5)
        
        1. ##### [.htaccess Information Leak](#alert-type-3) (1)
            
            1. GET https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/.htaccess
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [WSTG-v42-CONF-05](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/05-Enumerate_Infrastructure_and_Application_Admin_Interfaces)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|htaccess files can be used to alter the configuration of the Apache Web Server software to enable/disable additional functionality and features that the Apache Web Server software has to offer.|
                |Request|Request line and header section (607 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/.htaccess HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0<br>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8<br>Accept-Language: en-US,en;q=0.5<br>Connection: keep-alive<br>Referer: https://public-firing-range.appspot.com/dom/index.html<br>Upgrade-Insecure-Requests: 1<br>Sec-Fetch-Dest: document<br>Sec-Fetch-Mode: navigate<br>Sec-Fetch-Site: same-origin<br>Sec-Fetch-User: ?1<br>Content-Length: 0<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (501 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: 13cf3fbaeb222f40b1ff0fd36014dc3e<br>Date: Tue, 11 Oct 2022 19:58:21 GMT<br>Server: Google Frontend<br>Content-Length: 63<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (63 bytes)<br><br>```<br>Invalid Input. Only word characters ([a-zA-Z0-9_]) are allowed.<br>```|
                |Evidence|```<br>HTTP/1.1 200 OK<br>```|
                |Solution|Ensure the .htaccess file is not accessible.|
                
        2. ##### [Format String Error](#alert-type-9) (1)
            
            1. GET https://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack?callback=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A03](https://owasp.org/Top10/A03_2021-Injection/)<br>- [OWASP_2017_A01](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html)|
                |Alert description|A Format String error occurs when the submitted data of an input string is evaluated as a command by the application.|
                |Other info|Potential Format String Error. The script closed the connection on a /%s|
                |Request|Request line and header section (644 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack?callback=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0<br>Accept: */*<br>Accept-Language: en-US,en;q=0.5<br>Connection: keep-alive<br>Referer: https://public-firing-range.appspot.com/flashinjection/index.html<br>Sec-Fetch-Dest: script<br>Sec-Fetch-Mode: no-cors<br>Sec-Fetch-Site: same-origin<br>Content-Length: 0<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (374 bytes)<br><br>```<br>HTTP/1.1 500 Internal Server Error<br>X-Cloud-Trace-Context: 0f49114998ae0a78d0098ebba7be4349<br>Date: Tue, 11 Oct 2022 19:54:00 GMT<br>Content-Type: text/html<br>Server: Google Frontend<br>Content-Length: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (0 bytes)|
                |Parameter|```<br>callback<br>```|
                |Attack|```<br>ZAP%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s<br>```|
                |Solution|Rewrite the background program using proper deletion of bad character strings. This will require a recompile of the background executable.|
                
        3. ##### [Missing Anti-clickjacking Header](#alert-type-10) (1)
            
            1. GET https://public-firing-range.appspot.com
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [WSTG-v42-CLNT-09](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.|
                |Request|Request line and header section (230 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (458 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 074807e4900f2a8ee4825671b397ea7b<br>Server: Google Frontend<br>Content-Length: 1780<br>Date: Tue, 11 Oct 2022 19:01:10 GMT<br>Expires: Tue, 11 Oct 2022 19:11:10 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1780 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br><title>Firing Range</title><br></head><br><body><br>   <h1>Version 0.48</h1><br>   <h1>What is the Firing Range?</h1><br>   <p><br>     Firing Range is a test bed for automated web application security scanners. <br><br>     Its test cases are not meant<br>     to be hard to reach or exercise, as the site can be very easily crawlable. <br><br>     The testbed focuses on detection capabilities, presenting many variants of vulnerabilities and<br>     hard-to-detect edge cases.<br><br>     For more details, see the <a href="https://github.com/google/firing-range">GitHub page</a>.<br>  </p><br>  <ul><br>    <li><a href="/address/index.html">Address DOM XSS</a></li><br>    <li><a href="/angular/index.html">Angular-based XSSes</a></li><br>    <li><a href="/badscriptimport/index.html">Bad JavaScript imports</a></li><br>    <li><a href="/cors/index.html">CORS related vulnerabilities</a></li><br>    <li><a href="/dom/index.html">DOM XSS</a></li><br>    <li><a href="/escape/index.html">Escaped XSS</a></li><br>    <li><a href="/flashinjection/index.html">Flash Injection</a></li><br>    <li><a href="/mixedcontent/index.html">Mixed content</a></li><br>    <li><a href="/redirect/index.html">Redirect XSS</a></li><br>    <li><a href="/reflected/index.html">Reflected XSS</a></li><br>    <li><a href="/remoteinclude/index.html">Remote inclusion XSS</a></li><br>    <li><a href="/reverseclickjacking/">Reverse ClickJacking</a></li><br>    <li><a href="/tags/index.html">Tag based XSS</a></li><br>    <li><a href="/urldom/index.html">URL-based DOM XSS</a></li><br>    <li><a href="/vulnerablelibraries/index.html">Vulnerable libraries</a></li><br>    <li><a href="/leakedcookie/index.html">Leaked httpOnly cookie</a></li><br>    <li><a href="/invalidframingconfig/index.html">Invalid framing configuration</a></li><br>  </ul><br></body><br></html><br>```|
                |Parameter|```<br>X-Frame-Options<br>```|
                |Solution|Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.<br><br>If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.|
                
        4. ##### [Secure Pages Include Mixed Content (Including Scripts)](#alert-type-11) (1)
            
            1. GET https://public-firing-range.appspot.com/mixedcontent/index.html
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)<br>- [WSTG-v42-CRYP-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/03-Testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels)|
                |Alert description|The page includes mixed content, that is content accessed via HTTP instead of HTTPS.|
                |Other info|tag=script src=http://public-firing-range.appspot.com/mixedcontent/script.js|
                |Request|Request line and header section (305 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/mixedcontent/index.html HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (457 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 36815d1200a5c10964caef3240dc62eb<br>Server: Google Frontend<br>Content-Length: 422<br>Date: Tue, 11 Oct 2022 19:01:19 GMT<br>Expires: Tue, 11 Oct 2022 19:11:19 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (422 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br><title>Firing Range - Mixed Content</title><br><script src="http://public-firing-range.appspot.com/mixedcontent/script.js"><br></script><br></head><br><body><br>  <div class="intro"><br>    <p><br>      This page contains a <code>script</code> tag which sources a script over<br>      HTTP. This creates a mixed content vulnerability when the page itself is<br>      opened via HTTPS.<br>    </p><br>  </div><br></body><br></html><br>```|
                |Evidence|```<br>http://public-firing-range.appspot.com/mixedcontent/script.js<br>```|
                |Solution|A page that is available over SSL/TLS must be comprised completely of content which is transmitted over SSL/TLS.<br><br>The page must not contain any content that is transmitted over unencrypted HTTP.<br><br>This includes content from third party sites.|
                
        5. ##### [X-Frame-Options Setting Malformed](#alert-type-12) (1)
            
            1. GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnoframeancestors
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [WSTG-v42-CLNT-09](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|An X-Frame-Options header was present in the response but the value was not correctly set.|
                |Request|Request line and header section (362 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/invalidframingconfig/xfoallowfromnoframeancestors HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/invalidframingconfig/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (530 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Frame-Options: ALLOW-FROM https://example.com<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: d2b25dbf1bc962a9751b52be4cfcdb72<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 137<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (137 bytes)<br><br>```<br><!DOCTYPE html><br><title>Invalid framing configuration</title><br>X-Frame-Options ALLOW-FROM is set but there is no CSP frame-ancestors entry.<br>```|
                |Parameter|```<br>X-Frame-Options<br>```|
                |Evidence|```<br>ALLOW-FROM https://example.com<br>```|
                |Solution|Ensure a valid setting is used on all web pages returned by your site (if you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.|
                
5. ### Risk=Medium, Confidence=Low (1)
    
    1. #### https://public-firing-range.appspot.com (1)
        
        1. ##### [Absence of Anti-CSRF Tokens](#alert-type-4) (1)
            
            1. GET https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)<br>- [WSTG-v42-SESS-05](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery)<br>- [OWASP_2017_A05](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html)|
                |Alert description|No Anti-CSRF tokens were found in a HTML submission form.<br><br>A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.<br><br>CSRF attacks are effective in a number of situations, including:<br><br>* The victim has an active session on the target site.<br><br>* The victim is authenticated via HTTP auth on the target site.<br><br>* The victim is on the same local network as the target site.<br><br>CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.|
                |Other info|No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "q" ].|
                |Request|Request line and header section (335 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0 HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/angular/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (502 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: 8fbc0dfb3281e84b25ab9c96dab7845e<br>Date: Tue, 11 Oct 2022 19:01:27 GMT<br>Server: Google Frontend<br>Content-Length: 266<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (266 bytes)<br><br>```<br><html ng-app><br>  <body><br>    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js"></script><br>    <form action="" method="post"><br>      <input type="text" name="q"><br>      <input type="submit"><br>    </form><br>    <div><br>      <br>    </div><br>  </body><br></html><br>```|
                |Evidence|```<br><form action="" method="post"><br>```|
                |Solution|Phase: Architecture and Design<br><br>Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.<br><br>For example, use anti-CSRF packages such as the OWASP CSRFGuard.<br><br>Phase: Implementation<br><br>Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.<br><br>Phase: Architecture and Design<br><br>Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).<br><br>Note that this can be bypassed using XSS.<br><br>Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.<br><br>Note that this can be bypassed using XSS.<br><br>Use the ESAPI Session Management control.<br><br>This control includes a component for CSRF.<br><br>Do not use the GET method for any request that triggers a state change.<br><br>Phase: Implementation<br><br>Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.|
                
6. ### Risk=Low, Confidence=Medium (6)
    
    1. #### https://public-firing-range.appspot.com (6)
        
        1. ##### [Application Error Disclosure](#alert-type-13) (1)
            
            1. GET https://public-firing-range.appspot.com/reflected/parameter/body/500?q=a
                
                |   |   |
                |---|---|
                |Alert tags|- [WSTG-v42-ERRH-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/02-Testing_for_Stack_Traces)<br>- [WSTG-v42-ERRH-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/01-Testing_For_Improper_Error_Handling)<br>- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.|
                |Request|Request line and header section (334 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/reflected/parameter/body/500?q=a HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/reflected/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (520 bytes)<br><br>```<br>HTTP/1.1 500 Internal Server Error<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: 2b35db95304025317e3e16207146240b<br>Date: Tue, 11 Oct 2022 19:01:38 GMT<br>Server: Google Frontend<br>Content-Length: 39<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (39 bytes)<br><br>```<br><html><br>  <body><br>    a<br>  </body><br></html><br>```|
                |Evidence|```<br>HTTP/1.1 500 Internal Server Error<br>```|
                |Solution|Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.|
                
        2. ##### [Cookie Without Secure Flag](#alert-type-14) (1)
            
            1. GET https://public-firing-range.appspot.com/leakedcookie/leakedcookie
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [WSTG-v42-SESS-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.|
                |Request|Request line and header section (330 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/leakedcookie/leakedcookie HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/leakedcookie/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (534 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>Set-Cookie: my_secret_cookie=2w/VTcGfRZA=; HttpOnly<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: 00ff2c334e77dee4d7dd25ef797daf44<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 196<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (196 bytes)<br><br>```<br><!DOCTYPE html><br><title>Leaking httpOnly cookie from the Set-Cookie header in the body</title><br>This page contains the value of the httpOnly cookie that is set in the response<br>header:<br><br>2w/VTcGfRZA=<br>```|
                |Parameter|```<br>my_secret_cookie<br>```|
                |Evidence|```<br>Set-Cookie: my_secret_cookie<br>```|
                |Solution|Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted channel. Ensure that the secure flag is set for cookies containing such sensitive information.|
                
        3. ##### [Cookie without SameSite Attribute](#alert-type-15) (1)
            
            1. GET https://public-firing-range.appspot.com/leakedcookie/leakedcookie
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)<br>- [WSTG-v42-SESS-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes)<br>- [OWASP_2017_A05](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html)|
                |Alert description|A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.|
                |Request|Request line and header section (330 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/leakedcookie/leakedcookie HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/leakedcookie/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (534 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>Set-Cookie: my_secret_cookie=2w/VTcGfRZA=; HttpOnly<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: 00ff2c334e77dee4d7dd25ef797daf44<br>Date: Tue, 11 Oct 2022 19:01:56 GMT<br>Server: Google Frontend<br>Content-Length: 196<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (196 bytes)<br><br>```<br><!DOCTYPE html><br><title>Leaking httpOnly cookie from the Set-Cookie header in the body</title><br>This page contains the value of the httpOnly cookie that is set in the response<br>header:<br><br>2w/VTcGfRZA=<br>```|
                |Parameter|```<br>my_secret_cookie<br>```|
                |Evidence|```<br>Set-Cookie: my_secret_cookie<br>```|
                |Solution|Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.|
                
        4. ##### [Cross-Domain JavaScript Source File Inclusion](#alert-type-16) (1)
            
            1. GET https://public-firing-range.appspot.com/angular/angular_body/1.2.0?q=test
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A08](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)|
                |Alert description|The page includes one or more script files from a third-party domain.|
                |Request|Request line and header section (333 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/angular/angular_body/1.2.0?q=test HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/angular/index.html<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (502 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: f8d24e569052f2f3c040567765f25c93<br>Date: Tue, 11 Oct 2022 19:01:26 GMT<br>Server: Google Frontend<br>Content-Length: 164<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (164 bytes)<br><br>```<br><html ng-app><br>  <body><br>    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js"></script><br>    <div><br>      {{test}}<br>    </div><br>  </body><br></html><br>```|
                |Parameter|```<br>//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js<br>```|
                |Evidence|```<br><script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js"></script><br>```|
                |Solution|Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.|
                
        5. ##### [Private IP Disclosure](#alert-type-17) (1)
            
            1. GET https://public-firing-range.appspot.com/badscriptimport/index.html
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)<br>- [OWASP_2017_A03](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure.html)|
                |Alert description|A private IP (such as 10.x.x.x, 172.x.x.x, 192.168.x.x) or an Amazon EC2 private hostname (for example, ip-10-0-56-78) has been found in the HTTP response body. This information might be helpful for further attacks targeting internal systems.|
                |Other info|192.168.1.2<br><br>192.168.1.2|
                |Request|Request line and header section (308 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/badscriptimport/index.html HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (458 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 3f718fa3e82a1171c606b3e84898e71d<br>Server: Google Frontend<br>Content-Length: 1071<br>Date: Tue, 11 Oct 2022 19:01:16 GMT<br>Expires: Tue, 11 Oct 2022 19:11:16 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1071 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br>  <title>Firing Range - Bad import of JavaScript sources</title><br></head><br><body><br><body><br>  These vulnerabilities import JavaScript from bad sources that are not<br>  necessarily owned by the page owner. For more details, see<br>  <a href="http://blog.securitee.org/?p=255">http://blog.securitee.org/?p=255</a>.<br><br>  <ul><br>    <li><br>      Script inclusions from locahost, for example<br>      <a href="/remoteinclude/parameter/script?q=http://127.0.0.2/localhost_import.js"><br>        http://127.0.0.2/localhost_import.js</a><br>    </li><br>    <li><br>      Script inclusions from private-network IP addresses, for example<br>      <a href="/remoteinclude/parameter/script?q=http://192.168.1.2/private_network_import.js"><br>        http://192.168.1.2/private_network_import.js</a><br>    </li><br>    <li><br>      Script inclusions from non-registered domains or typosquatting domains, for example<br>      <a href="/remoteinclude/parameter/script?q=http://g00gle.com/typosquatting_domain.js"><br>        http://g00gle.com/typosquatting_domain.js</a><br>    </li><br>  </ul><br></body><br></html><br>```|
                |Evidence|```<br>192.168.1.2<br>```|
                |Solution|Remove the private IP address from the HTTP response body. For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.|
                
        6. ##### [X-Content-Type-Options Header Missing](#alert-type-18) (1)
            
            1. GET https://public-firing-range.appspot.com
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)<br>- [OWASP_2017_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)|
                |Alert description|The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.|
                |Other info|This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.<br><br>At "High" threshold this scan rule will not alert on client or server error responses.|
                |Request|Request line and header section (230 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (458 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 074807e4900f2a8ee4825671b397ea7b<br>Server: Google Frontend<br>Content-Length: 1780<br>Date: Tue, 11 Oct 2022 19:01:10 GMT<br>Expires: Tue, 11 Oct 2022 19:11:10 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1780 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br><title>Firing Range</title><br></head><br><body><br>   <h1>Version 0.48</h1><br>   <h1>What is the Firing Range?</h1><br>   <p><br>     Firing Range is a test bed for automated web application security scanners. <br><br>     Its test cases are not meant<br>     to be hard to reach or exercise, as the site can be very easily crawlable. <br><br>     The testbed focuses on detection capabilities, presenting many variants of vulnerabilities and<br>     hard-to-detect edge cases.<br><br>     For more details, see the <a href="https://github.com/google/firing-range">GitHub page</a>.<br>  </p><br>  <ul><br>    <li><a href="/address/index.html">Address DOM XSS</a></li><br>    <li><a href="/angular/index.html">Angular-based XSSes</a></li><br>    <li><a href="/badscriptimport/index.html">Bad JavaScript imports</a></li><br>    <li><a href="/cors/index.html">CORS related vulnerabilities</a></li><br>    <li><a href="/dom/index.html">DOM XSS</a></li><br>    <li><a href="/escape/index.html">Escaped XSS</a></li><br>    <li><a href="/flashinjection/index.html">Flash Injection</a></li><br>    <li><a href="/mixedcontent/index.html">Mixed content</a></li><br>    <li><a href="/redirect/index.html">Redirect XSS</a></li><br>    <li><a href="/reflected/index.html">Reflected XSS</a></li><br>    <li><a href="/remoteinclude/index.html">Remote inclusion XSS</a></li><br>    <li><a href="/reverseclickjacking/">Reverse ClickJacking</a></li><br>    <li><a href="/tags/index.html">Tag based XSS</a></li><br>    <li><a href="/urldom/index.html">URL-based DOM XSS</a></li><br>    <li><a href="/vulnerablelibraries/index.html">Vulnerable libraries</a></li><br>    <li><a href="/leakedcookie/index.html">Leaked httpOnly cookie</a></li><br>    <li><a href="/invalidframingconfig/index.html">Invalid framing configuration</a></li><br>  </ul><br></body><br></html><br>```|
                |Parameter|```<br>X-Content-Type-Options<br>```|
                |Solution|Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.<br><br>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.|
                
7. ### Risk=Informational, Confidence=Low (2)
    
    1. #### https://public-firing-range.appspot.com (2)
        
        1. ##### [Information Disclosure - Suspicious Comments](#alert-type-19) (1)
            
            1. GET https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback/
                
                |   |   |
                |---|---|
                |Alert tags|- [OWASP_2021_A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)<br>- [OWASP_2017_A03](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure.html)|
                |Alert description|The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.|
                |Other info|The following pattern was used: \bFROM\b and was detected in the element starting with: "<script><br><br>var resultDiv = document.getElementById('result');<br><br>/**<br><br>* Callback function that receives data from th", see evidence field for the suspicious comment/snippet.|
                |Request|Request line and header section (364 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback/ HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br>Referer: https://public-firing-range.appspot.com/reverseclickjacking/<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (503 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-XSS-Protection: 0<br>Cache-Control: no-cache, no-store, must-revalidate<br>Pragma: no-cache<br>Expires: Thu, 01 Jan 1970 00:00:00 GMT<br>Content-Type: text/html;charset=utf-8<br>X-Cloud-Trace-Context: fac2b40dfef60d30ba83aad814aa68ed<br>Date: Tue, 11 Oct 2022 19:01:47 GMT<br>Server: Google Frontend<br>Content-Length: 1552<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1552 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br>  <title>Universal Reverse Clickjacking - single page, parameter in the<br>  fragment</title><br></head><br><br><body><br>  <div><br>    <button id='urc_button' onclick='alert(42)'>Button with side<br>    effects</button><br>  </div><br><br>  <div id='result'></div><br>  <script><br>    var resultDiv = document.getElementById('result');<br><br>      /**<br>       * Callback function that receives data from the JSONP callback and<br>       * prints a "stringified" representation of the response, just for<br>       * human debugging.<br>       */<br>      function callbackFunc(data) {<br>        resultDiv.textContent = 'JSONP data received: ' + JSON.stringify(data);<br>      }<br><br>      try {<br>        // Retrieve the "q" parameter in the URL fragment<br>        var q = decodeURIComponent(new RegExp('[?&#]q=([^&]*)')<br>            .exec(location.hash)[1]);<br><br>        // Validate it (prevents trivial XSS)<br>        var allowedPattern = /^[a-zA-Z0-9\._&#=]+$/;<br>        if (allowedPattern.test(q)) {<br>          // The vulnerability arises because of this insecure concatenation<br>          var url = '/reverseclickjacking/jsonpendpoint?q=' + q<br>              + '&callback=' + q + '';<br><br>          /* Create the <script> tag that executes the JS code returned by<br>           * the JSONP endpoint. */<br>          var s = document.createElement('script');<br>          s.type = 'text/javascript';<br>          s.src = url;<br>          document.body.appendChild(s);<br>        }<br>      } catch(e) {<br>        resultDiv.textContent = 'Please specify a q parameter in the fragment.';<br>      }<br>  </script><br></body><br></html><br>```|
                |Evidence|```<br>from<br>```|
                |Solution|Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.|
                
        2. ##### [Re-examine Cache-control Directives](#alert-type-20) (1)
            
            1. GET https://public-firing-range.appspot.com
                
                |   |   |
                |---|---|
                |Alert tags|- [WSTG-v42-ATHN-06](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses)|
                |Alert description|The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.|
                |Request|Request line and header section (230 bytes)<br><br>```<br>GET https://public-firing-range.appspot.com HTTP/1.1<br>Host: public-firing-range.appspot.com<br>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0<br>Pragma: no-cache<br>Cache-Control: no-cache<br><br>```<br><br>Request body (0 bytes)|
                |Response|Status line and header section (458 bytes)<br><br>```<br>HTTP/1.1 200 OK<br>X-Cloud-Trace-Context: 074807e4900f2a8ee4825671b397ea7b<br>Server: Google Frontend<br>Content-Length: 1780<br>Date: Tue, 11 Oct 2022 19:01:10 GMT<br>Expires: Tue, 11 Oct 2022 19:11:10 GMT<br>Cache-Control: public, max-age=600<br>ETag: "dtC-HA"<br>Content-Type: text/html<br>Age: 0<br>Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"<br><br>```<br><br>Response body (1780 bytes)<br><br>```<br><!DOCTYPE html><br><html><br><head><br><title>Firing Range</title><br></head><br><body><br>   <h1>Version 0.48</h1><br>   <h1>What is the Firing Range?</h1><br>   <p><br>     Firing Range is a test bed for automated web application security scanners. <br><br>     Its test cases are not meant<br>     to be hard to reach or exercise, as the site can be very easily crawlable. <br><br>     The testbed focuses on detection capabilities, presenting many variants of vulnerabilities and<br>     hard-to-detect edge cases.<br><br>     For more details, see the <a href="https://github.com/google/firing-range">GitHub page</a>.<br>  </p><br>  <ul><br>    <li><a href="/address/index.html">Address DOM XSS</a></li><br>    <li><a href="/angular/index.html">Angular-based XSSes</a></li><br>    <li><a href="/badscriptimport/index.html">Bad JavaScript imports</a></li><br>    <li><a href="/cors/index.html">CORS related vulnerabilities</a></li><br>    <li><a href="/dom/index.html">DOM XSS</a></li><br>    <li><a href="/escape/index.html">Escaped XSS</a></li><br>    <li><a href="/flashinjection/index.html">Flash Injection</a></li><br>    <li><a href="/mixedcontent/index.html">Mixed content</a></li><br>    <li><a href="/redirect/index.html">Redirect XSS</a></li><br>    <li><a href="/reflected/index.html">Reflected XSS</a></li><br>    <li><a href="/remoteinclude/index.html">Remote inclusion XSS</a></li><br>    <li><a href="/reverseclickjacking/">Reverse ClickJacking</a></li><br>    <li><a href="/tags/index.html">Tag based XSS</a></li><br>    <li><a href="/urldom/index.html">URL-based DOM XSS</a></li><br>    <li><a href="/vulnerablelibraries/index.html">Vulnerable libraries</a></li><br>    <li><a href="/leakedcookie/index.html">Leaked httpOnly cookie</a></li><br>    <li><a href="/invalidframingconfig/index.html">Invalid framing configuration</a></li><br>  </ul><br></body><br></html><br>```|
                |Parameter|```<br>Cache-Control<br>```|
                |Evidence|```<br>public, max-age=600<br>```|
                |Solution|For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".|
                

## Appendix

### Alert types

This section contains additional information on the types of alerts in the report.

1. #### Cross Site Scripting (DOM Based)
    
    |   |   |
    |---|---|
    |Source|raised by an active scanner ([Cross Site Scripting (DOM Based)](https://www.zaproxy.org/docs/alerts/40026/))|
    |CWE ID|[79](https://cwe.mitre.org/data/definitions/79.html)|
    |WASC ID|8|
    |Reference|1. [http://projects.webappsec.org/Cross-Site-Scripting](http://projects.webappsec.org/Cross-Site-Scripting)<br>2. [http://cwe.mitre.org/data/definitions/79.html](http://cwe.mitre.org/data/definitions/79.html)|
    
2. #### Cross Site Scripting (Reflected)
    
    |   |   |
    |---|---|
    |Source|raised by an active scanner ([Cross Site Scripting (Reflected)](https://www.zaproxy.org/docs/alerts/40012/))|
    |CWE ID|[79](https://cwe.mitre.org/data/definitions/79.html)|
    |WASC ID|8|
    |Reference|1. [http://projects.webappsec.org/Cross-Site-Scripting](http://projects.webappsec.org/Cross-Site-Scripting)<br>2. [http://cwe.mitre.org/data/definitions/79.html](http://cwe.mitre.org/data/definitions/79.html)|
    
3. #### External Redirect
    
    |   |   |
    |---|---|
    |Source|raised by an active scanner ([External Redirect](https://www.zaproxy.org/docs/alerts/20019/))|
    |CWE ID|[601](https://cwe.mitre.org/data/definitions/601.html)|
    |WASC ID|38|
    |Reference|1. [http://projects.webappsec.org/URL-Redirector-Abuse](http://projects.webappsec.org/URL-Redirector-Abuse)<br>2. [http://cwe.mitre.org/data/definitions/601.html](http://cwe.mitre.org/data/definitions/601.html)|
    
4. #### .htaccess Information Leak
    
    |   |   |
    |---|---|
    |Source|raised by an active scanner ([.htaccess Information Leak](https://www.zaproxy.org/docs/alerts/40032/))|
    |CWE ID|[94](https://cwe.mitre.org/data/definitions/94.html)|
    |WASC ID|14|
    |Reference|1. [http://www.htaccess-guide.com/](http://www.htaccess-guide.com/)|
    
5. #### Absence of Anti-CSRF Tokens
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Absence of Anti-CSRF Tokens](https://www.zaproxy.org/docs/alerts/10202/))|
    |CWE ID|[352](https://cwe.mitre.org/data/definitions/352.html)|
    |WASC ID|9|
    |Reference|1. [http://projects.webappsec.org/Cross-Site-Request-Forgery](http://projects.webappsec.org/Cross-Site-Request-Forgery)<br>2. [http://cwe.mitre.org/data/definitions/352.html](http://cwe.mitre.org/data/definitions/352.html)|
    
6. #### CSP: Wildcard Directive
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([CSP](https://www.zaproxy.org/docs/alerts/10055/))|
    |CWE ID|[693](https://cwe.mitre.org/data/definitions/693.html)|
    |WASC ID|15|
    |Reference|1. [http://www.w3.org/TR/CSP2/](http://www.w3.org/TR/CSP2/)<br>2. [http://www.w3.org/TR/CSP/](http://www.w3.org/TR/CSP/)<br>3. [http://caniuse.com/#search=content+security+policy](http://caniuse.com/#search=content+security+policy)<br>4. [http://content-security-policy.com/](http://content-security-policy.com/)<br>5. [https://github.com/shapesecurity/salvation](https://github.com/shapesecurity/salvation)<br>6. [https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)|
    
7. #### CSP: script-src unsafe-inline
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([CSP](https://www.zaproxy.org/docs/alerts/10055/))|
    |CWE ID|[693](https://cwe.mitre.org/data/definitions/693.html)|
    |WASC ID|15|
    |Reference|1. [http://www.w3.org/TR/CSP2/](http://www.w3.org/TR/CSP2/)<br>2. [http://www.w3.org/TR/CSP/](http://www.w3.org/TR/CSP/)<br>3. [http://caniuse.com/#search=content+security+policy](http://caniuse.com/#search=content+security+policy)<br>4. [http://content-security-policy.com/](http://content-security-policy.com/)<br>5. [https://github.com/shapesecurity/salvation](https://github.com/shapesecurity/salvation)<br>6. [https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)|
    
8. #### CSP: style-src unsafe-inline
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([CSP](https://www.zaproxy.org/docs/alerts/10055/))|
    |CWE ID|[693](https://cwe.mitre.org/data/definitions/693.html)|
    |WASC ID|15|
    |Reference|1. [http://www.w3.org/TR/CSP2/](http://www.w3.org/TR/CSP2/)<br>2. [http://www.w3.org/TR/CSP/](http://www.w3.org/TR/CSP/)<br>3. [http://caniuse.com/#search=content+security+policy](http://caniuse.com/#search=content+security+policy)<br>4. [http://content-security-policy.com/](http://content-security-policy.com/)<br>5. [https://github.com/shapesecurity/salvation](https://github.com/shapesecurity/salvation)<br>6. [https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)|
    
9. #### Content Security Policy (CSP) Header Not Set
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Content Security Policy (CSP) Header Not Set](https://www.zaproxy.org/docs/alerts/10038/))|
    |CWE ID|[693](https://cwe.mitre.org/data/definitions/693.html)|
    |WASC ID|15|
    |Reference|1. [https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy](https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy)<br>2. [https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)<br>3. [http://www.w3.org/TR/CSP/](http://www.w3.org/TR/CSP/)<br>4. [http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html](http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html)<br>5. [http://www.html5rocks.com/en/tutorials/security/content-security-policy/](http://www.html5rocks.com/en/tutorials/security/content-security-policy/)<br>6. [http://caniuse.com/#feat=contentsecuritypolicy](http://caniuse.com/#feat=contentsecuritypolicy)<br>7. [http://content-security-policy.com/](http://content-security-policy.com/)|
    
10. #### Format String Error
    
    |   |   |
    |---|---|
    |Source|raised by an active scanner ([Format String Error](https://www.zaproxy.org/docs/alerts/30002/))|
    |CWE ID|[134](https://cwe.mitre.org/data/definitions/134.html)|
    |WASC ID|6|
    |Reference|1. [https://owasp.org/www-community/attacks/Format_string_attack](https://owasp.org/www-community/attacks/Format_string_attack)|
    
11. #### Missing Anti-clickjacking Header
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Anti-clickjacking Header](https://www.zaproxy.org/docs/alerts/10020/))|
    |CWE ID|[1021](https://cwe.mitre.org/data/definitions/1021.html)|
    |WASC ID|15|
    |Reference|1. [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)|
    
12. #### Secure Pages Include Mixed Content (Including Scripts)
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Secure Pages Include Mixed Content](https://www.zaproxy.org/docs/alerts/10040/))|
    |CWE ID|[311](https://cwe.mitre.org/data/definitions/311.html)|
    |WASC ID|4|
    |Reference|1. [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)|
    
13. #### X-Frame-Options Setting Malformed
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Anti-clickjacking Header](https://www.zaproxy.org/docs/alerts/10020/))|
    |CWE ID|[1021](https://cwe.mitre.org/data/definitions/1021.html)|
    |WASC ID|15|
    |Reference|1. [https://tools.ietf.org/html/rfc7034#section-2.1](https://tools.ietf.org/html/rfc7034#section-2.1)|
    
14. #### Application Error Disclosure
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Application Error Disclosure](https://www.zaproxy.org/docs/alerts/90022/))|
    |CWE ID|[200](https://cwe.mitre.org/data/definitions/200.html)|
    |WASC ID|13|
    
15. #### Cookie Without Secure Flag
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Cookie Without Secure Flag](https://www.zaproxy.org/docs/alerts/10011/))|
    |CWE ID|[614](https://cwe.mitre.org/data/definitions/614.html)|
    |WASC ID|13|
    |Reference|1. [https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html)|
    
16. #### Cookie without SameSite Attribute
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Cookie without SameSite Attribute](https://www.zaproxy.org/docs/alerts/10054/))|
    |CWE ID|[1275](https://cwe.mitre.org/data/definitions/1275.html)|
    |WASC ID|13|
    |Reference|1. [https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site)|
    
17. #### Cross-Domain JavaScript Source File Inclusion
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Cross-Domain JavaScript Source File Inclusion](https://www.zaproxy.org/docs/alerts/10017/))|
    |CWE ID|[829](https://cwe.mitre.org/data/definitions/829.html)|
    |WASC ID|15|
    
18. #### Private IP Disclosure
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Private IP Disclosure](https://www.zaproxy.org/docs/alerts/2/))|
    |CWE ID|[200](https://cwe.mitre.org/data/definitions/200.html)|
    |WASC ID|13|
    |Reference|1. [https://tools.ietf.org/html/rfc1918](https://tools.ietf.org/html/rfc1918)|
    
19. #### X-Content-Type-Options Header Missing
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([X-Content-Type-Options Header Missing](https://www.zaproxy.org/docs/alerts/10021/))|
    |CWE ID|[693](https://cwe.mitre.org/data/definitions/693.html)|
    |WASC ID|15|
    |Reference|1. [http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx](http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx)<br>2. [https://owasp.org/www-community/Security_Headers](https://owasp.org/www-community/Security_Headers)|
    
20. #### Information Disclosure - Suspicious Comments
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Information Disclosure - Suspicious Comments](https://www.zaproxy.org/docs/alerts/10027/))|
    |CWE ID|[200](https://cwe.mitre.org/data/definitions/200.html)|
    |WASC ID|13|
    
21. #### Re-examine Cache-control Directives
    
    |   |   |
    |---|---|
    |Source|raised by a passive scanner ([Re-examine Cache-control Directives](https://www.zaproxy.org/docs/alerts/10015/))|
    |CWE ID|[525](https://cwe.mitre.org/data/definitions/525.html)|
    |WASC ID|13|
    |Reference|1. [https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)<br>2. [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)<br>3. [https://grayduck.mn/2021/09/13/cache-control-recommendations/](https://grayduck.mn/2021/09/13/cache-control-recommendations/)|