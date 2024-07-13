from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to provide the correct path to the WebDriver executable)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

try:
    # Open the webpage
    driver.get("https://www.saucedemo.com/")
    
    # Find the username field and enter the username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    
    # Find the password field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    
    # Find the login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Wait for a moment to ensure the page loads completely
    time.sleep(3)
    
    # Fetch the title of the webpage
    title = driver.title
    
    # Fetch the current URL of the webpage
    current_url = driver.current_url
    
    # Extract the entire contents of the webpage
    page_source = driver.page_source
    
    # Save the page contents to a text file
    with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(page_source)
    
    # Print the results
    print("Title of the webpage:", title)
    print("Current URL of the webpage:", current_url)

finally:
    # Close the WebDriver
    driver.quit()
