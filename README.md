# SubShot

SubShot is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters to collect and gather subdomains for a particular domain, apply HTTP & HTTPS Probing to filter working URLs and also capture a screenshot of every website.

The screenshot utility uses Selenium's Chrome Headless driver.

SubShot enumerates subdomains using the following search engines and websites: 
> Google, Yahoo, Bing, Baidu, Ask, Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.

Based on Python 3.8.3 and compiled using python's own virtualenv.

## Installation

To install dependencies:

~~~
pip install pyqt5 argparse requests dnspython chromedriver selenium webdriver_manager
~~~

To run SubShot:

1. Using source file:
~~~
python3 run.py
~~~

2. Using Windows executable:
~~~
!!! Coming Soon !!!
~~~
