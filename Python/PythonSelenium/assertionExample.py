from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Girish") --> this is depricated in selenium 4
driver.find_element(By.NAME, "name").send_keys("Girish")
driver.find_element(By.ID, "exampleCheck1").click()

# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# select class can only be used if we have tag-name as select

dropdown.select_by_index(0)

driver.find_element(By.NAME, "email").send_keys("testEmail@gmail.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "success" in message    # we are checking substring here which we discuss in PythonBasics

driver.close()
