from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys('admin123')
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()

action_chains = ActionChains(driver)
action_chains.move_to_element(driver.find_element(By.XPATH, "//a[@id='menu_leave_viewLeaveModule']")).perform()
action_chains.move_to_element(driver.find_element(By.XPATH, "//a[@id='menu_leave_Reports']")).perform()

driver.find_element(By.ID, "menu_leave_viewLeaveBalanceReport").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.forward()
time.sleep(10)
driver.find_element(By.XPATH, "//a[@id='welcome']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()

driver.quit()
