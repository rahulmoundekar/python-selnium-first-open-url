# Selenium With Python :

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.

Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 2.7, 3.5 and above.
What is webdriver?
Selenium WebDriver is an automation testing tool. When I say automation, it means it automates test scripts written in Selenium.

#### Pre Requisites

  - Making the project as :
    ```
    mkdir python-selnium-first-open-url
	cd python-selnium-first-open-url
    ```
  - environment installation:
     ```
     open command prompt type 
        pip install virtualenv
     create virtualenv
    	>>virtualenv selenium-setup
     we need to activate virtualenv for use
    	>>selenium-setup\scripts\activate
     
    
    pip install selenium
    ```
    While the installation of Selenium makes the functionality available to you, you need additional drivers for it to be able to interface with a chosen web browser. The download links for the drivers are available here: Chrome, Edge, Firefox and Safari. For the remainder of this tutorial, we will use the Chrome driver. Follow the link for the browser of your choice and download the driver for the compatible version.
    
#### Drivers

Selenium requires a driver to interface with the chosen browser.
All supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.    

Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

 - In order to execute code
