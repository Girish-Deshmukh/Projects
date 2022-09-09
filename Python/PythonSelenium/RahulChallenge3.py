import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list1 = []
list2 = []
s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# names = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
# for name in names:
#     print(name.text)    --> this is also one method but the below one is more maintainable


# //div[@class='product-action']/button/parent::div/parent::div/h4
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    list1.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
print(list1)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
names2 = driver.find_elements(By.XPATH, '//p[@class="product-name"]')

for name in names2:
    list2.append(name.text)
print(list2)
if list1 == list2:
    print("the lists are matching")
else:
    print("the lists are not matching")

OriginalAmt = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
DiscountAmt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(float(DiscountAmt))
print(int(OriginalAmt))
assert float(DiscountAmt) < int(OriginalAmt)

amounts = driver.find_elements(By.XPATH, "//tr//td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

print(sum)
TotalAmt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == TotalAmt
driver.close()

