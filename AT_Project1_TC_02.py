from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set the path to your chromedriver executable
chrome_driver = webdriver.Chrome()  # chrome_driver is to open the browser , it's a driver object
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(10)  # max wait time for the website to load

# Navigate to the Orange HRM login page
chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
chrome_driver.implicitly_wait(10)  # max wait time for the website to load

# Find the username and password input fields and the login button
username_field = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
password_field = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
login_button = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]')

# Enter your credentials
username_field.send_keys('xxxx')
password_field.send_keys('yyyy')

# Click the login button
login_button.click()

print("Invalid login credentials")

# Add a delay to see the result before closing the browser
time.sleep(5)

# Close the browser
chrome_driver.quit()
