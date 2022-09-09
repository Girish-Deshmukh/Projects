from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Girish")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("Deshmukh")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
driver.find_element(By.NAME, "cancel").click()
print(driver.find_element(By.XPATH, "//*[@id='login_form']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(4)").text)

# Practice projects --> https://rahulshettyacademy.com/#/practice-project
