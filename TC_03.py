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

# # Find and Click the admin button
# admin = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
# admin.click()
# time.sleep(5)

admin = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').is_displayed()

pim = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').is_displayed()

leave = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').is_displayed()

Time = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').is_displayed()

recruitment = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').is_displayed()

my_info = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').is_displayed()

performance = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').is_displayed()

dashboard = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').is_displayed()

directory = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').is_displayed()

maintenance = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').is_displayed()

buzz = chrome_driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').is_displayed()

if (admin and pim and leave and time and recruitment and my_info and performance and dashboard and directory and
        maintenance and buzz):
    print("Admin\npim\nleave\ntime\nrecruitment\nmy info\nperformance\ndash board\ndirectory\nmaintenance\nbuzz\n "
          "are displayed")

else:

    print("not found")
