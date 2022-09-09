import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")


for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        #Add item into cart
        product.find_element(By.XPATH, "div[2]/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
# wait = WebDriverWait(driver, 60)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//*[@class='media-heading'])[1]")))
PhoneCheck = driver.find_element(By.XPATH, "(//*[@class='media-heading'])[1]").text
assert "Blackberry" in PhoneCheck
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
# driver.find_element(By.ID, "checkbox2").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
driver.find_element(By.XPATH, "//*[@class='btn btn-success btn-lg']").click()
print(driver.find_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']").text)




