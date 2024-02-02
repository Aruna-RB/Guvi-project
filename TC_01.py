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

forgot_password = chrome_driver.find_element(By.CLASS_NAME, 'orangehrm-login-forgot')

forgot_password.click()

time.sleep(10)

titles = (chrome_driver.find_element
          (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys('Aruna'))

time.sleep(5)

reset_password = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

reset_password.click()

time.sleep(5)

verification = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/p[1]/p')

print(verification)

assert verification.text == "A reset password link has been sent to you via email."

# Add a delay to see the result before closing the browser
time.sleep(5)

# Close the browser
chrome_driver.quit()
