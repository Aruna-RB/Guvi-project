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

# Enter invalid credentials
username_field.send_keys('Admin')
password_field.send_keys('admin123')

# Click the login button
login_button.click()

# Find and Click the admin button
admin = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
admin.click()
time.sleep(5)

# Validate options displayed on main page
try:
    assert chrome_driver.title == "OrangeHRM"
    print("Title verified correctly")
except:
    print("Title Mismatched")

time.sleep(5)

# Options displayed on Admin page
User_management = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').is_displayed()

Job = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').is_displayed()

Organization = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').is_displayed()

Qualification = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').is_displayed()

# Nationalities=chrome_driver.find_element(
#   By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').is_displayed()

Corporate_Banking = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]').is_displayed()

Configuration = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span').is_displayed()

if User_management and Job and Organization and Qualification and Corporate_Banking and Configuration:
    print("User management\njob\norganization\nqualifications\ncorporate banking\nconfiguration options are displayed"
          " on admin page")
else:
    print("not found")
