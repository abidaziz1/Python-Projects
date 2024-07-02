from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define the path to your Chrome WebDriver
driver_path = "F:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(driver_path)

# Maximize the browser window
driver.maximize_window()

# Open the Google homepage
driver.get("https://www.google.com")

# Find the search box element using the 'name' attribute
search_box = driver.find_element(By.NAME, "q")

# Type the search query "Selenium Python" into the search box
search_box.send_keys("Selenium Python")

# Simulate pressing the Enter key to submit the search query
search_box.send_keys(Keys.RETURN)

# Wait until the search results are loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

# Take a screenshot of the search results page
driver.save_screenshot("google_search_results.png")

# Find and print the titles of the search results
titles = driver.find_elements(By.CSS_SELECTOR, "h3")
for title in titles:
    print(title.text)

# Example of interacting with elements using ActionChains
first_result = titles[0]
actions = ActionChains(driver)
actions.move_to_element(first_result).perform()

# Example of handling browser navigation
driver.back()  # Navigate back
time.sleep(2)
driver.forward()  # Navigate forward
time.sleep(2)
driver.refresh()  # Refresh the page
time.sleep(2)

# Example of handling multiple windows/tabs
driver.execute_script("window.open('https://www.selenium.dev', '_blank');")
driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
time.sleep(2)
driver.close()  # Close the current tab
driver.switch_to.window(driver.window_handles[0])  # Switch back to the original tab

# Example of handling alerts
# (Note: This requires a site with an alert to be triggered)
# driver.execute_script("alert('This is an alert');")
# alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert.accept()  # Accept the alert

# Example of managing cookies
cookies = driver.get_cookies()  # Get all cookies
print(cookies)
driver.add_cookie({"name": "test_cookie", "value": "test_value"})  # Add a cookie
print(driver.get_cookie("test_cookie"))  # Get a specific cookie
driver.delete_cookie("test_cookie")  # Delete a specific cookie
driver.delete_all_cookies()  # Delete all cookies

# Example of executing JavaScript
title = driver.execute_script("return document.title;")
print(f"Page title is: {title}")

# Example of extracting data for web scraping
descriptions = driver.find_elements(By.CSS_SELECTOR, "span.aCOpRe")
for description in descriptions:
    print(description.text)

# Clean up: close the browser
driver.quit()