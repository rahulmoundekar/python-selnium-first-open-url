from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://jqueryui.com/droppable/")
element = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(element)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()
time.sleep(10)
driver.quit()
