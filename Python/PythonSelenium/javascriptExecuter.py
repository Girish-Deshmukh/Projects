# Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

ShopButton = driver.find_element(By.XPATH, "(//a[@class='nav-link'])[2]")
driver.execute_script("arguments[0].click();", ShopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

