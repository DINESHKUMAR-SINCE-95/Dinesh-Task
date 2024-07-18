from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests

# Setup WebDriver
driver = webdriver.Chrome()

# Task 1: CoWIN Website Operations
driver.get("https://www.cowin.gov.in/")

# Find and click the "FAQ" link to open in a new window
faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
faq_link.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)

# Find and click the "Partners" link to open in a new window
partners_link = driver.find_element(By.LINK_TEXT, "Partners")
partners_link.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)

# Get window handles
main_window = driver.current_window_handle
all_windows = driver.window_handles

# Print the window handles
print("All Window Handles:", all_windows)

# Close the newly opened windows and return to the main window
for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        driver.close()

driver.switch_to.window(main_window)


# Task 2: Labour Ministry Website Operations
driver.get("https://labour.gov.in/")

# Find and click the "Documents" menu to download the Monthly Progress Report
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
documents_menu.click()

# Assuming there is a link to download the Monthly Progress Report
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_link.click()

# Find and click the "Media" menu to go to the Photo Gallery
media_menu = driver.find_element(By.LINK_TEXT, "Media")
media_menu.click()

# Find and click the "Photo Gallery" sub-menu
photo_gallery_link = driver.find_element(By.LINK_TEXT, "Photo Gallery")
photo_gallery_link.click()

# Download 10 photos from the Photo Gallery
photo_elements = driver.find_elements(By.TAG_NAME, "img")[:10]
photo_urls = [photo.get_attribute('src') for photo in photo_elements]

# Create a folder to store the photos
folder_name = "downloaded_photos"
os.makedirs(folder_name, exist_ok=True)

# Download and save the photos
for index, url in enumerate(photo_urls):
    response = requests.get(url)
    with open(f"{folder_name}/photo_{index+1}.jpg", 'wb') as file:
        file.write(response.content)

# Close the driver
driver.quit()
