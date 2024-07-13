from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace 'path/to/webdriver' with the actual path to your WebDriver executable
driver = webdriver.Chrome(executable_path='path/to/webdriver')

try:
    # Open the website
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)

    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    for cookie in cookies_before_login:
        print(cookie)

    # Perform login
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    # Display cookies after login
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    for cookie in cookies_after_login:
        print(cookie)

    # Perform logout
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    time.sleep(2)

    # Display cookies after logout
    cookies_after_logout = driver.get_cookies()
    print("\nCookies after logout:")
    for cookie in cookies_after_logout:
        print(cookie)

finally:
    driver.quit()
