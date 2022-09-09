from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
childwindow = driver.window_handles[1]  # ("parentId", "childId")

driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
driver.close()
