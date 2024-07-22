# Import necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for testing
service = Service('https://www.orangehrm.com/')  # Update with the path to your ChromeDriver

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open the OrangeHRM portal
    driver.get('http://example.com/orangehrm')  # Update with the actual URL

    # Step 2: Enter username
    username_field = driver.find_element(By.ID, 'txtUsername')
    username_field.send_keys('Admin')

    # Step 3: Enter password
    password_field = driver.find_element(By.ID, 'txtPassword')
    password_field.send_keys('admin123')

    # Step 4: Click the login button
    login_button = driver.find_element(By.ID, 'btnLogin')
    login_button.click()

    # Validate the login is successful by checking the presence of a dashboard element
    assert "Dashboard" in driver.title

    print("Test Passed: User logged in successfully")
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    # Close the browser
    driver.quit()
