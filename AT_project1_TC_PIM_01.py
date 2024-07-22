from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the web driver
driver = webdriver.Chrome() 
driver.maximize_window()

# Precondition: Login to Orange HRM
def login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUsername"))).send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

# Test Steps
def add_employee(driver, first_name, last_name, employee_id):
    # Go to PIM module
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_pim_viewPimModule"))).click()

    # Click on Add Employee
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_pim_addEmployee"))).click()

    # Fill in employee details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "employeeId").clear()
    driver.find_element(By.ID, "employeeId").send_keys(employee_id)

    # Save employee details
    driver.find_element(By.ID, "btnSave").click()

    # Verify successful addition
    success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message.success"))).text
    assert "Successfully Saved" in success_message, "Employee was not added successfully."

# Execute the test case
try:
    login(driver, "valid_username", "valid_password")
    add_employee(driver, "John", "Doe", "12345")
    print("Test case TC_PIM_01 passed.")
except Exception as e:
    print(f"Test case TC_PIM_01 failed: {e}")
finally:
    driver.quit()
