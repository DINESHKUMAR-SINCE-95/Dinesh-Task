#To create the Selenium test cases for the OrangeHRM login scenarios in Python, we will cover both positive and negative scenarios. Below are the details for the test cases:

### Test Case: TC_Login_01
#**Test Objective:**
#Successful Employee login to OrangeHRM portal.

#**Precondition:**
#1. A valid ESS-User account to login to be available.
#2. OrangeHRM 3.0 site is launched on a compatible browser.

#**Steps:**
#1. In the login Panel, enter the username (Test Data: "Admin").
#2. Enter the Password for the ESS-User account in the password field (Test data: "admin123").
#3. Click "Login" button.

#**Expected Result:**
#The user is logged in successfully.

### Test Case: TC_Login_02
#**Test Objective:**
#Unsuccessful login with invalid username.

#**Steps:**
#1. In the login Panel, enter the invalid username (Test Data: "InvalidUser").
#2. Enter the Password for the ESS-User account in the password field (Test data: "admin123").
#. Click "Login" button.

#**Expected Result:**
#An error message is displayed for invalid username.

### Test Case: TC_Login_03
#**Test Objective:**
#Unsuccessful login with invalid password.

#**Steps:**
#1. In the login Panel, enter the username (Test Data: "Admin").
#2. Enter the invalid Password for the ESS-User account in the password field (Test data: "invalidPassword").
#3. Click "Login" button.

#**Expected Result:**
#An error message is displayed for invalid password.

#### Test Case: TC_Login_04
#**Test Objective:**
#Unsuccessful login with empty username.

#**Steps:**
#1. In the login Panel, leave the username field empty.
#2. Enter the Password for the ESS-User account in the password field (Test data: "admin123").
#3. Click "Login" button.

#*Expected Result:**
#An error message is displayed for empty username.

### Test Case: TC_Login_05
#*Test Objective:**
#Unsuccessful login with empty password.

#**Steps:**
#1. In the login Panel, enter the username (Test Data: "Admin").
#2. Leave the password field empty.
#3. Click "Login" button.

#**Expected Result:**
#An error message is displayed for empty password.

#Here is a Python script using Selenium to automate these test cases:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Launch the OrangeHRM website
driver.get("http://example.com/orangehrm")

def login_test(username, password, expected_result):
    try:
        # Locate the username field and enter the username
        username_field = driver.find_element(By.ID, "txtUsername")
        username_field.clear()
        username_field.send_keys(username)
        
        # Locate the password field and enter the password
        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click the login button
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        
        if expected_result == "success":
            # Wait for the dashboard to be visible after login
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "welcome"))
            )
            print("Test passed: User logged in successfully.")
        else:
            # Wait for the error message to be visible
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "spanMessage"))
            )
            print(f"Test passed: Error message displayed - {error_message.text}")
    except Exception as e:
        print(f"Test failed: {str(e)}")

# Test Case TC_Login_01: Successful login
login_test("Admin", "admin123", "success")

# Test Case TC_Login_02: Invalid username
login_test("InvalidUser", "admin123", "failure")

# Test Case TC_Login_03: Invalid password
login_test("Admin", "invalidPassword", "failure")

# Test Case TC_Login_04: Empty username
login_test("", "admin123", "failure")

# Test Case TC_Login_05: Empty password
login_test("Admin", "", "failure")

# Close the WebDriver
driver.quit()


#This script covers the specified test cases, including fetching error messages for invalid logins. Ensure the web elements' IDs (e.g., `txtUsername`, `txtPassword`, `btnLogin`, `spanMessage`) match those in your OrangeHRM system. Adjust these identifiers if necessary.


#To automate this test case using Python Selenium, you can follow these steps. Make sure you have the Selenium library installed (`pip install selenium`) and the WebDriver for your chosen browser (like ChromeDriver) set up correctly.

#Here's a basic script outline:

# Test case ID: TC Login_ 02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

try:
    # Navigate to the OrangeHRM login page
    driver.get("https://example.com/login")

    # Fill in the username
    username_input = driver.find_element(By.ID, "txtUsername")
    username_input.send_keys("Admin*")

    # Fill in the password
    password_input = driver.find_element(By.ID, "txtPassword")
    password_input.send_keys("Invalid password")

    # Click on the login button
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()

    # Wait for the error message element to appear
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-message-id"))
    )

    # Assert or verify the error message text
    assert "Invalid credentials" in error_message.text

    # Optionally, take a screenshot or further assertions

finally:
    # Close the browser window
    driver.quit()

# Test case ID: TC PIM_01

### Notes:
# - Replace `"https://example.com/login"` with the actual URL of your OrangeHRM login page.
#- Replace `By.ID`, `"txtUsername"`, `"txtPassword"`, `"btnLogin"`, and `"error-message-id"` with the actual IDs or other locators used in your HTML.
#- Use `WebDriverWait` to ensure that elements are loaded before interacting with them.
#- Adjust the error message verification (`assert` statement) based on the actual error message displayed on the page.

#This script provides a basic framework. You might need to adjust it based on the specific HTML structure and behavior of your OrangeHRM login page.


#To automate this test case for adding a new employee in the PIM module using Python Selenium, you can follow these steps:

#Step-by-Step Implementation
#Setup Selenium WebDriver
#Make sure you have Selenium installed (pip install selenium) and the appropriate WebDriver for your chosen browser.

#Initialize WebDriver
#Initialize an instance of the WebDriver (e.g., Chrome).

#Login to OrangeHRM
#Navigate to the OrangeHRM login page and log in using valid credentials.

#Navigate to PIM Module
#Go to the PIM module from the left pane.

#Add New Employee
#Click on "Add" and fill in the employee details.

#Verify Success Message
#Verify the success message after adding the employee.

#Full Example Script
#Here's the complete script to automate the test case:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the OrangeHRM login page
    driver.get("https://example.com/login")  # Replace with actual URL

    # Step 2: Login to OrangeHRM
    username = "valid_username"  # Replace with actual username
    password = "valid_password"  # Replace with actual password

    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

    # Step 3: Navigate to PIM module
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule")))
    driver.find_element(By.ID, "menu_pim_viewPimModule").click()

    # Step 4: Click on Add button to add new employee
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "btnAdd")))
    driver.find_element(By.ID, "btnAdd").click()

    # Step 5: Fill in employee details
    first_name = "John"
    last_name = "Doe"
    employee_id = "1234"

    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "employeeId").clear()
    driver.find_element(By.ID, "employeeId").send_keys(employee_id)

    # Step 6: Save the new employee details
    driver.find_element(By.ID, "btnSave").click()

    # Step 7: Verify the success message
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))
    success_message = driver.find_element(By.XPATH, "//div[@class='message success fadable']").text
    assert "Successfully Saved" in success_message

    # Optionally, take a screenshot or further assertions

finally:
    # Close the browser window
    driver.quit()

#Notes:
#Replace "https://example.com/login" with the actual URL of your OrangeHRM login page.
#Replace By.ID, By.XPATH, and other locators with the actual identifiers used in your HTML.
#Adjust the username and password variables with valid credentials.
#Adjust the employee details (first_name, last_name, employee_id) as needed.
#Use WebDriverWait to ensure that elements are loaded before interacting with them.
#Verify the success message based on the actual message displayed on the page.
#This script provides a structured approach to automating the process of adding a new employee in the PIM module using Selenium in Python. Adjustments may be needed based on the specific structure and behavior of your application.



#  Test case ID: TC PIM_02

#To automate the test case for editing an existing employee in the PIM module using Python Selenium, follow these steps:

### Step-by-Step Implementation

#1. **Setup Selenium WebDriver**: Install Selenium (`pip install selenium`) and the appropriate WebDriver (e.g., ChromeDriver).

#2. **Initialize WebDriver**: Initialize an instance of the WebDriver (e.g., Chrome).

#3. **Login to OrangeHRM**: Navigate to the OrangeHRM login page and log in using valid credentials.

#4. **Navigate to PIM Module**: Go to the PIM module from the left pane.

#5. **Edit Existing Employee**: Locate an existing employee, edit their information, and save the changes.

#6. **Verify Success Message**: Verify the success message after editing the employee details.

### Full Example Script

#Here's the complete script to automate the test case:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the OrangeHRM login page
    driver.get("https://example.com/login")  # Replace with actual URL

    # Step 2: Login to OrangeHRM
    username = "valid_username"  # Replace with actual username
    password = "valid_password"  # Replace with actual password

    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

    # Step 3: Navigate to PIM module
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule")))
    driver.find_element(By.ID, "menu_pim_viewPimModule").click()

    # Step 4: Search and select an existing employee
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "empsearch_employee_name_empName")))
    search_input = driver.find_element(By.ID, "empsearch_employee_name_empName")
    search_input.send_keys("John Doe")  # Replace with the actual employee name to search

    driver.find_element(By.ID, "searchBtn").click()

    # Step 5: Click on the employee name to edit
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "John Doe")))  # Adjust locator as needed
    driver.find_element(By.LINK_TEXT, "John Doe").click()  # Adjust locator as needed

    # Step 6: Edit employee information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "btnSave")))
    driver.find_element(By.ID, "btnSave").click()

    # Edit the necessary fields (example: last name)
    last_name_input = driver.find_element(By.ID, "personal_txtEmpLastName")
    last_name_input.clear()
    last_name_input.send_keys("UpdatedLastName")  # Replace with the new last name

    # Save the changes
    driver.find_element(By.ID, "btnSave").click()

    # Step 7: Verify the success message
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))
    success_message = driver.find_element(By.XPATH, "//div[@class='message success fadable']").text
    assert "Successfully Saved" in success_message

finally:
    # Close the browser window
    driver.quit()


### Notes:

#- Replace `"https://example.com/login"` with the actual URL of your OrangeHRM login page.
#- Replace `By.ID`, `By.XPATH`, and other locators with the actual identifiers used in your HTML.
#- Adjust the `username` and `password` variables with valid credentials.
#- Adjust the search input and employee selection steps according to the actual structure of your employee list.
#- Modify the employee information fields (e.g., `last_name_input`) according to the fields you need to edit.
#- Use `WebDriverWait` to ensure that elements are loaded before interacting with them.
#- Verify the success message based on the actual message displayed on the page.

#This script provides a # structured approach to automating the process of editing an existing employee in the PIM module using Selenium in Python. Adjustments may be needed based on the specific structure and behavior of your application.


# Lest case ID: TC_PIM_03

#To automate the test case for deleting an existing employee in the PIM module using Python Selenium, you can follow these steps:

#Step-by-Step Implementation
#Setup Selenium WebDriver: Install Selenium (pip install selenium) and the appropriate WebDriver (e.g., ChromeDriver).

#Initialize WebDriver: Initialize an instance of the WebDriver (e.g., Chrome).

#Login to OrangeHRM: Navigate to the OrangeHRM login page and log in using valid credentials.

#Navigate to PIM Module: Go to the PIM module from the left pane.

#Delete Existing Employee: Locate an existing employee, delete them, and confirm the deletion.

#Verify Success Message: Verify the success message after deleting the employee.
#
#Full Example Script
#Here's the complete script to automate the test case:



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the OrangeHRM login page
    driver.get("https://example.com/login")  # Replace with actual URL

    # Step 2: Login to OrangeHRM
    username = "valid_username"  # Replace with actual username
    password = "valid_password"  # Replace with actual password

    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

    # Step 3: Navigate to PIM module
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule")))
    driver.find_element(By.ID, "menu_pim_viewPimModule").click()

    # Step 4: Search for an existing employee to delete
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "empsearch_employee_name_empName")))
    search_input = driver.find_element(By.ID, "empsearch_employee_name_empName")
    search_input.send_keys("John Doe")  # Replace with the actual employee name to search

    driver.find_element(By.ID, "searchBtn").click()

    # Step 5: Select the employee from the search results
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='John Doe']")))  # Adjust locator as needed
    driver.find_element(By.XPATH, "//a[text()='John Doe']").click()  # Adjust locator as needed

    # Step 6: Click on the Delete button
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "btnDelete")))
    driver.find_element(By.ID, "btnDelete").click()

    # Confirm the deletion in the modal
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dialogDeleteBtn")))
    driver.find_element(By.ID, "dialogDeleteBtn").click()

    # Step 7: Verify the success message
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))
    success_message = driver.find_element(By.XPATH, "//div[@class='message success fadable']").text
    assert "Successfully Deleted" in success_message

finally:
    # Close the browser window
    driver.quit()


#Notes:
#Replace "https://example.com/login" with the actual URL of your OrangeHRM login page.
#Replace By.ID, By.XPATH, and other locators with the actual identifiers used in your HTML.
#Adjust the username and password variables with valid credentials.
#Adjust the search input and employee selection steps according to the actual structure of your employee list.
#Modify the employee information fields and button locators as necessary based on the actual web page structure.
#Use WebDriverWait to ensure that elements are loaded before interacting with them.
#Verify the success message based on the actual message displayed on the page.
# This script provides a structured approach to automating the process of deleting an existing employee in the PIM module using Selenium in Python. Adjustments may be needed based on the specific structure and behavior of your application




