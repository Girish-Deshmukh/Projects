from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
Menu = driver.find_element(By.ID, "mousehover")
action.move_to_element(Menu).perform()
# ChildMenu = driver.find_element(By.LINK_TEXT, 'Top')
ChildMenu = driver.find_element(By.LINK_TEXT, 'Reload')
action.move_to_element(ChildMenu).click().perform()

