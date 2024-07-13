from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver (e.g., ChromeDriver)
driver_path = 'path/to/your/chromedriver'

# Initialize the WebDriver
driver = webdriver.Chrome(driver_path)

# Open Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Give some time for the page to load
time.sleep(3)

# Login to Instagram
username_input = driver.find_element(By.XPATH, "//input[@name='username']")
password_input = driver.find_element(By.XPATH, "//input[@name='password']")

# Replace these with your Instagram username and password
username = 'your_instagram_username'
password = 'your_instagram_password'

username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Give some time for the login to complete
time.sleep(5)

# Open the target Instagram page
driver.get('https://www.instagram.com/guviofficial/')

# Give some time for the page to load
time.sleep(3)

# Extract Followers and Following counts using XPATH
followers_xpath = '//a[contains(@href, "/followers")]/span'
following_xpath = '//a[contains(@href, "/following")]/span'

followers_count = driver.find_element(By.XPATH, followers_xpath).get_attribute('title')
following_count = driver.find_element(By.XPATH, following_xpath).text

print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the WebDriver
driver.quit()
