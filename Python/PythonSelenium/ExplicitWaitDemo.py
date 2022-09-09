import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

validateText = "Option3"

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
output = driver.find_element(By.CSS_SELECTOR, "span[class='promoInfo']").text
print(output)
