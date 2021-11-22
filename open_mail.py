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
all_elements = driver.find_element(By.TAG_NAME, 'tbody')
trs = all_elements.find_elements(By.TAG_NAME,'tr')
print(len(trs))
print(trs[1].get_attribute('innerHTML'))
sec_td = trs[1].find_elements(By.TAG_NAME,'td')
sec_td[1].find_element(By.TAG_NAME,'input').send_keys("sadasdsa")



#all_elements.send_keys("asdsaad")