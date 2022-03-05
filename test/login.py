from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("F:\pythonselenium\\firstselenium\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
driver.find_element(By.ID, "ap_email").send_keys("jannatulferdusm786@gmail.com")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "ap_password").send_keys("abc123")
driver.find_element(By.ID, "signInSubmit").click()




time.sleep(4)
driver.close()
