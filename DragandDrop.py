from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://iqueryui.com/droppable/")

# Switch to the frame containing the draggable and droppable elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform drag and drop
action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable, droppable).perform()

# Close the browser
driver.quit()
