# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Setup the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Launch the OrangeHRM site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
driver.maximize_window()
time.sleep(3)  # Wait for the page to load

# Step 1: Enter the username
username_field = driver.find_element(By.ID, "txtUsername")  
username_field.send_keys("Admin")

# Step 2: Enter the invalid password
password_field = driver.find_element(By.ID, "txtPassword")  
password_field.send_keys("Invalid password")

# Step 3: Click the "Login" button
login_button = driver.find_element(By.ID, "btnLogin") 
login_button.click()

# Expected Result: Check for the error message
time.sleep(2)  # Wait for the error message to appear
error_message = driver.find_element(By.ID, "spanMessage")  
# Validate the error message
expected_message = "Invalid credentials"   
assert error_message.text == expected_message, f"Expected '{expected_message}', but got '{error_message.text}'"

print("Test passed: Valid error message for invalid credentials is displayed.")

# Close the browser
driver.quit()
