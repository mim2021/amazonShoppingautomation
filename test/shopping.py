import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("F:\pythonselenium\\firstselenium\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com/")
driver.maximize_window()
driver.get("https://www.amazon.com/")
# shoppinfoptionselect
driver.find_element(By.XPATH, "//a[@aria-label='Computers & Accessories']").click()
# scrolldown
driver.execute_script("window.scrollTo(0, 1250)")
# chooseanoption
driver.find_element(By.XPATH, "//a[@href='/Logitech-MK270-Wireless-Keyboard-Mouse/dp/B079JLY5M5/ref=lp_16225007011_1_7']").click()
# addtocart
driver.find_element(By.NAME, "submit.add-to-registry.wishlist.unrecognized").click()
# signinwithemail
driver.find_element(By.ID, "ap_email").send_keys("jannatulferdusm786@gmail.com")
#clickcontinuebutton
driver.find_element(By.ID, "continue").click()
# password
driver.find_element(By.ID, "ap_password").send_keys("abcc123")
# clicksigninbutton
driver.find_element(By.ID, "auth-signin-button").click()
# clickaddtolist
driver.find_element(By.ID, "add-to-wishlist-button-submit").click()

driver.find_element(By.NAME, "a-button-input a-declarative").click()
# viewlist
driver.find_element(By.CLASS_NAME, "a-button-text").click()

time.sleep(4)
driver.close()