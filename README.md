# SubShot

This tool provides the following functionalities:
* Subdomain enumeration using OSINT
* HTTP & HTTPS probing
* Hostile subdomain takeover possibility
* Screenshotting subdomains using Selenium's Chrome Headless driver

SubShot enumerates subdomains using the following search engines and websites: 
> Google, Yahoo, Bing, Baidu, Ask, Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.

## Installation

To install dependencies:

~~~
pip install pyqt5 argparse requests dnspython chromedriver selenium webdriver_manager
~~~

You'll also need ruby which can be installed using:

~~~
sudo apt install ruby-full // Debian/Ubuntu-based distros
sudo pacman -S ruby // Arch-based distros
~~~

To run SubShot:

1. Using source file: `python3 main.py`

2. Using executable: `Coming Soon`
