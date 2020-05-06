from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys('admin123')
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()

driver.find_element(By.XPATH, "//a[@id='welcome']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()

driver.quit()
