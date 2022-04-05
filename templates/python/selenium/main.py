'''
Docs for Selenium module: https://selenium-python.readthedocs.io/
First make sure to run 'pip install -r requirements.txt' and install webdriver:
 -  Chrome   -->  https://sites.google.com/chromium.org/driver/
 -  Edge     -->  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
 -  Firefox  -->  https://github.com/mozilla/geckodriver/releases
 -  Safari   -->  https://webkit.org/downloads/
'''
from selenium import webdriver

# Chromedriver
driver = webdriver.Chrome(executable_path=r"YOUR_PATH_TO_CHROMEDRIVER")
driver.get("http://www.python.org")

# Edge driver
driver = webdriver.Edge(executable_path=r"YOUR_PATH_TO_EDGEDRIVER")
driver.get("http://www.python.org")

# Firefox driver
driver = webdriver.Firefox(executable_path=r"YOUR_PATH_TO_FIREFOXDRIVER")
driver.get("http://www.python.org")

# Safari driver
driver = webdriver.Safari(executable_path=r"YOUR_PATH_TO_SAFARIDRIVER")
driver.get("http://www.python.org")

driver.quit()