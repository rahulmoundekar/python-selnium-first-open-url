from selenium import webdriver

# create a new Chrome session
driver = webdriver.Chrome(executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://opensource-demo.orangehrmlive.com/")

# get the of application home page
print(driver.title)

# The next line is an assertion to confirm that title has “OrangeHRM” word in it:
assert "OrangeHRM" in driver.title

# close the current instance of browser window
driver.close()

# close the all open instance of browser window
driver.quit()