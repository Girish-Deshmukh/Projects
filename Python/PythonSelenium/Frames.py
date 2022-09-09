from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
# iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
#  frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH, "//body[@id='tinymce']").clear()
driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys(" I am able to Automate")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()