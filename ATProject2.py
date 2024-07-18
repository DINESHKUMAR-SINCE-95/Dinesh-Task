#Test case ID: TC_PIM_01

#To validate the "Forgot Password" link on the Orange HRM 3.0 site using Python Selenium, you can follow these steps:

#Launch the URL.
#Click on the "Forgot Password" link.
#Check if the username textbox is visible.
#Provide the username.
#Click on the "Reset Password" button.
#Verify that a successful message is displayed saying "Reset Password link sent successfully".
#Here's a complete script to automate this test scenario:

#Step-by-Step Python Script
#Install Selenium: If you haven't already, install Selenium using pip:

#bash
#Copy code
#pip install selenium
#Download WebDriver: Make sure you have the appropriate WebDriver for your browser. For example, download ChromeDriver for Google Chrome and make sure it is in your system PATH.

#Write the Script:

#python
#Copy code


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Replace 'path/to/webdriver' with the actual path to your WebDriver executable
driver = webdriver.Chrome(executable_path='path/to/webdriver')

try:
    Launch URL
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(2)  # Wait for the page to load

    Click on "Forgot Password" link
    forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot your password?')
    forgot_password_link.click()
    time.sleep(2)  # Wait for the forgot password page to load

    Check if the username textbox is visible
    username_textbox = driver.find_element(By.NAME, 'username')
    if username_textbox.is_displayed():
        print("Username textbox is visible.")
    else:
        print("Username textbox is not visible.")
        driver.quit()
        exit()

    Provide the username
    username_textbox.send_keys('your_username')  # Replace 'your_username' with a valid username

    Click on Reset Password button
    reset_password_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    reset_password_button.click()
    time.sleep(2)  # Wait for the response

    Check for the successful message
    success_message = driver.find_element(By.XPATH, '//*[contains(text(), "Reset Password link sent successfully")]')
    if success_message.is_displayed():
        print("Reset Password link sent successfully.")
    else:
        print("Success message not found.")

finally:
    driver.quit()


#Test case ID: TC_PIN 02

#Explanation:
#Launch URL:

#The script sets up the WebDriver and opens the https://opensource-demo.orangehrmlive.com/web/index.php/auth/login URL.
#Click on "Forgot Password" Link:

#The script locates the "Forgot your password?" link by its text and clicks it.
#Check if the Username Textbox is Visible:

#The script checks if the username textbox is visible on the "Forgot Password" page.
#Provide the Username:

#The script enters the username into the textbox.
#Click on Reset Password Button:

#The script locates the "Reset Password" button by its type and clicks it.
#Verify the Successful Message:

#The script checks for a successful message saying "Reset Password link sent successfully".
#Notes:
#Adjust the time.sleep() duration as necessary based on your network speed and website responsiveness.
#Replace 'your_username' with a valid username for the Orange HRM demo site.
#Make sure the path to the WebDriver executable is correct.
#This script automates the validation of the "Forgot Password" link on the Orange HRM 3.0 site and verifies that the expected result is achieved. Let me know if you have any questions or need further assistance!

#To achieve this using Selenium in Python, you'll need to follow these steps:

#Set up your environment by installing Selenium and the necessary web driver for your browser.
#Create a Python script to perform the steps you've outlined.
# Here is a basic example script that performs the actions you described:



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Precondition: Launch URL and Login as "Admin"
def login(driver, url, username, password):
    driver.get(url)
    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

Step 1: Go to Admin page and Validate "Title" of the page as OrangeHRM*
def validate_admin_page(driver):
    driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
    
    # Validate Title
    WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))
    assert "OrangeHRM" in driver.title, "Title does not match"

    # Step 2: Validate the options
    options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking", "Configuration"]
    for option in options:
        element = driver.find_element(By.XPATH, f"//*[text()='{option}']")
        assert element.is_displayed(), f"{option} is not displayed on the Admin page"

def main():
    url = "http://your-orangehrm-site-url"
    username = "Admin"
    password = "admin_password"

    driver = webdriver.Chrome()  # Make sure you have the appropriate driver installed
    driver.maximize_window()

    try:
        login(driver, url, username, password)
        validate_admin_page(driver)
        print("Test Passed: All validations are successful.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
        

#if __name__ == "__main__":
    #main()
#Steps to run the script:

#Install Selenium:
#Open a terminal and install Selenium using pip:

#sh
#Copy code
#pip install selenium
#Download WebDriver:
#Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and make sure it is in your system PATH or specify the path in the script:

#python
#Copy code
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
#Update URL and Credentials:
#Replace "http://your-orangehrm-site-url", "Admin", and "admin_password" with the actual URL and credentials.

#Run the Script:
#Execute the Python script in your environment:

#sh
#Copy code
#python your_script_name.py
#This script will launch the Orange HRM site, log in as an admin, navigate to the Admin page, and validate that the specified headers are present.


#Test case ID: TC_PIM_03

#Here is a Python Selenium script that validates the main menu options on the Admin page of the Orange HRM 3.0 site:

#1. Launch URL and login as "Admin".
#2. Navigate to the Admin page.
#3. Validate the menu options on the side pane.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Precondition: Launch URL and Login as "Admin"
def login(driver, url, username, password):
    driver.get(url)
    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

# Step 1: Go to Admin page
def go_to_admin_page(driver):
    driver.find_element(By.ID, "menu_admin_viewAdminModule").click()

# Step 2: Validate the main menu options on the Admin page
def validate_menu_options(driver):
    menu_options = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory",
        "Maintenance",
        "Buzz"
    ]
    
    for option in menu_options:
        # Locate the menu option using its text
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{option}']"))
        )
        assert element.is_displayed(), f"{option} is not displayed on the Admin page"

def main():
    url = "http://your-orangehrm-site-url"
    username = "Admin"
    password = "admin_password"

    driver = webdriver.Chrome()  # Ensure you have the appropriate driver installed
    driver.maximize_window()

    try:
        login(driver, url, username, password)
        go_to_admin_page(driver)
        validate_menu_options(driver)
        print("Test Passed: All menu options are displayed on the Admin page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

#if __name__ == "__main__":
  #  main()


#Steps to run the script:



#1. Install Selenium:
 #  Open a terminal and install Selenium using pip:
  # ```sh
  # pip install selenium
  # ```

#2. Download WebDriver:
 #  Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and make sure it is in your system PATH or specify the path in the script:
 #  ```python
 #  driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
 #  ```

#3#.Update URL and Credentials:
 #  Replace `"http://your-orangehrm-site-url"`, `"Admin"`, and `"admin_password"` with the actual URL and credentials.

#4. Run the Script:
  # Execute the Python script in your environment:
 #  ```sh
 #  python your_script_name.py
  # ```

#This script will navigate to the Orange HRM site, log in as an admin, go to the Admin page, and validate that the specified menu options are present on the side pane of the Admin page.
