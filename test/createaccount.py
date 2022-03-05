import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("F:\pythonselenium\\firstselenium\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com/")
driver.maximize_window()
driver.get("https://www.amazon.com/")

driver.find_element(By.CLASS_NAME, "nav-line-1-container").click()
driver.find_element(By.ID, "createAccountSubmit").click()
driver.find_element(By.ID, "ap_customer_name").send_keys("Mim")
driver.find_element(By.ID, "ap_email").send_keys("jannatulferdusm786@gmail.com")
driver.find_element(By.ID, "ap_password").send_keys("abc123")
driver.find_element(By.ID, "ap_password_check").send_keys("abc123")
driver.find_element(By.ID, "continue").click()
time.sleep(4)
driver.close()
