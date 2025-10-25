from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()
driver.get("https://ronakjat.site/")
driver.maximize_window()

time.sleep(1)

name = driver.find_element(By.NAME, "from_name")
email = driver.find_element(By.NAME, "from_email")
message = driver.find_element(By.NAME, "message")


time.sleep(2)
name.send_keys("Hope")

time.sleep(2)
email.send_keys("hope0497@gmail.com")

time.sleep(2)
message.send_keys("Hello this is Hope . Let's talk")

pyautogui.click(989,999)
#button.click()

time.sleep(2)
driver.quit()
