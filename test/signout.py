import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("F:\pythonselenium\\firstselenium\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()
# sign in
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
driver.find_element(By.ID, "ap_email").send_keys("jannatulferdusm786@gmail.com")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "ap_password").send_keys("abc123")
driver.find_element(By.ID, "signInSubmit").click()
# mousehover
a = ActionChains(driver)
n = driver.find_element(By.ID, "nav-link-accountList")
a.move_to_element(n).perform()
# signout
driver.find_element(By.CLASS_NAME, "nav-line-2 ").click()

time.sleep(4)
# driver.close()
