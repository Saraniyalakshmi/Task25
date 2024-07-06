
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(500, 500);")



# expand all
expand_field_locator = (By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')
expand_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(expand_field_locator))
expand_field.click()
print("Menu option expanded successfully .")


# name field
name_field_locator = (By.NAME, 'name-text-input')
name_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(name_field_locator))
driver.execute_script("arguments[0].scrollIntoView();", name_field)
name_field.clear()
name_field.send_keys("john")
print("Name entered successfully.")


# Find the credit input element
credit_button = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit_button, "King")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()
print("credit entered successfully.")

# search button
search_locator = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button")
search_locator_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_locator))
driver.execute_script("arguments[0].scrollIntoView();", search_locator_button)
search_locator_button.click()

# Wait for results to load and keep them in view
results_locator = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul")
results = wait.until(EC.presence_of_all_elements_located(results_locator))
driver.execute_script("arguments[0].scrollIntoView();", results[0])

# Confirmation
print("Search performed successfully and results are in view")