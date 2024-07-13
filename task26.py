To automate the task using the Page Object Model (POM) along with Explicit Wait and Expected Conditions in Pytest, follow these steps:

1. Install Required Libraries:
   Ensure you have Selenium and Pytest installed. You can install them using pip:
   ```bash
   pip install selenium pytest
   ```

2. Set Up Your Project Structure:
   Create the following structure for your project:
   ```
   imdb_search/
   ├── pages/
   │   ├── __init__.py
   │   ├── search_page.py
   ├── tests/
   │   ├── __init__.py
   │   ├── test_search.py
   ├── conftest.py
   ├── pytest.ini
   ```

3. Configure `conftest.py:
   This file will handle the setup and teardown of the WebDriver.
   ```python
   import pytest
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service as ChromeService
   from webdriver_manager.chrome import ChromeDriverManager

   @pytest.fixture(scope="class")
   def driver_init(request):
       driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       request.cls.driver = driver
       yield
       driver.quit()
   ```

4. Create the Page Object (`search_page.py'):
   Define the elements and actions for the IMDB search page.
   ```python
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC

   class SearchPage:
       def __init__(self, driver):
           self.driver = driver
           self.url = "https://www.imdb.com/search/name/"
           self.name_input_locator = (By.ID, "name")
           self.birth_date_day_locator = (By.ID, "birth_day")
           self.birth_date_month_locator = (By.ID, "birth_month")
           self.birth_date_year_locator = (By.ID, "birth_year")
           self.role_select_locator = (By.ID, "role")
           self.search_button_locator = (By.XPATH, "//button[@type='submit']")

       def load(self):
           self.driver.get(self.url)

       def enter_name(self, name):
           name_input = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.name_input_locator))
           name_input.send_keys(name)

       def select_birth_date(self, day, month, year):
           day_select = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.birth_date_day_locator))
           month_select = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.birth_date_month_locator))
           year_select = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.birth_date_year_locator))

           day_select.send_keys(day)
           month_select.send_keys(month)
           year_select.send_keys(year)

       def select_role(self, role):
           role_select = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.role_select_locator))
           role_select.send_keys(role)

       def click_search(self):
           search_button = WebDriverWait(self.driver, 10).until(
               EC.element_to_be_clickable(self.search_button_locator))
           search_button.click()
   ```

5. Create the Test Case (`test_search.py`):
   Write the test using Pytest to perform the search.
   ```python
   import pytest
   from pages.search_page import SearchPage

   @pytest.mark.usefixtures("driver_init")
   class TestIMDBSearch:
       def test_search_by_name(self):
           search_page = SearchPage(self.driver)
           search_page.load()
           search_page.enter_name("Tom Hanks")
           search_page.select_birth_date("9", "July", "1956")
           search_page.select_role("Actor")
           search_page.click_search()

           # Add assertions here to validate the search results
   ```

6. Configure `pytest.ini`:
   Create a `pytest.ini` file to configure Pytest.
   ```ini
   [pytest]
   python_files = test_*.py
   python_classes = Test*
   python_functions = test_*
   ```

7. Run the Tests:
   Use the following command to run your tests:
   ```bash
   pytest
   ```

This setup uses the Page Object Model to encapsulate the web elements and actions on the IMDB search page, and it employs explicit waits to ensure that elements are present and interactable before performing actions.
