from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


validateText = "Option3"

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
print(alert.text)
alert.accept()  # for accepting the alert

driver.find_element(By.ID, "confirmbtn").click()
alert2 = driver.switch_to.alert
alert2.dismiss()


