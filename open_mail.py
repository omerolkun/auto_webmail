from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver



driver = webdriver.Chrome('/home/omergenc/TEST_BOARD/forSelenium/folder1/chromedriver')
driver.get("https://webmail.bilkent.edu.tr/")

print(driver.title)

email_field_id = "rcmloginuser"
password_field_id = "LoginForm-pd6135978ee"

email_field = driver.find_element(By.ID, email_field_id)
email_field.send_keys("omer.olkun@ug.bilkent.edu.tr")


sleep(1)
a = driver.find_elements_by_class_name("pass form-control")
print(a)
