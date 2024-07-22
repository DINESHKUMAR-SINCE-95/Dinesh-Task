# Install necessary packages
pip_package_installer({"__arg1": ["selenium"]})


# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define the test case
def test_login():
    # Set up the webdriver (assuming you have ChromeDriver installed and it's in your PATH)
    driver = webdriver.Chrome()

    try:
        # Open the OrangeHRM login page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with the actual URL of the OrangeHRM portal
        
        # Find the username field and enter the username
        username_field = driver.find_element(By.ID, "txtUsername")
        username_field.send_keys("Admin")
        
        # Find the password field and enter the password
        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.send_keys("admin123")
        
        # Find the login button and click it
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        
        # Wait for some time to ensure the login process completes
        time.sleep(3)
        
        # Check if the login was successful
        # This can be done by checking if a certain element that only appears after login is present
        try:
            welcome_message = driver.find_element(By.ID, "welcome")
            print("Login successful: Test Passed")
        except:
            print("Login failed: Test Failed")
    finally:
        # Close the browser
        driver.quit()

# Execute the test case
test_login()

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
