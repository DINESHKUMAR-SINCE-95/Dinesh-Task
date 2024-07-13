from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure WebDriver options
options = Options()
options.add_argument("--start-maximized")

# Specify the path to the chromedriver executable
chrome_driver_path = '/path/to/chromedriver'  # Update this path

# Initialize the Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the IMDb search page
    driver.get("https://www.imdb.com/search/name/")

    # Wait for the input boxes, select boxes, and drop down menu to be visible
    wait = WebDriverWait(driver, 10)

    # Fill in the data
    # Example: fill in the Name input box
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    name_input.send_keys("Leonardo DiCaprio")

    # Example: fill in the Birthplace input box
    birthplace_input = wait.until(EC.visibility_of_element_located((By.ID, "birth_place")))
    birthplace_input.send_keys("Los Angeles")

    # Example: select an option from the Gender dropdown menu
    gender_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "gender")))
    gender_dropdown.click()
    gender_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='gender']/option[@value='male']")))
    gender_option.click()

    # Example: fill in the Start Year input box
    start_year_input = wait.until(EC.visibility_of_element_located((By.ID, "start_year")))
    start_year_input.send_keys("1974")

    # Example: fill in the End Year input box
    end_year_input = wait.until(EC.visibility_of_element_located((By.ID, "end_year")))
    end_year_input.send_keys("2023")

    # Perform the search
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Search')]")))
    search_button.click()

    # Wait for the search results to be visible
    search_results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lister-list")))

    # Print out the search result titles
    results = driver.find_elements(By.XPATH, "//h3[@class='lister-item-header']/a")
    for result in results:
        print(result.text)

finally:
    # Close the WebDriver
    driver.quit()
