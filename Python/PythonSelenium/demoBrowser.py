from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# browser exposes an executable file
# through Selenium test we need to invoke the executable file which will then invoke actual browser

s=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
driver.close()
#driver.close will close only the current window
#driver.quit will close all the opened windows



