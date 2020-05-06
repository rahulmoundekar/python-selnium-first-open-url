from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID, 'txtUsername').send_keys('admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()

driver.find_element(By.ID, 'welcome').click()
driver.find_element(By.LINK_TEXT, 'Logout').click()

driver.quit()
