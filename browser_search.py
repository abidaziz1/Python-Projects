from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Path to the EdgeDriver executable
driver_path = "F:/edgedriver_win64/msedgedriver.exe"

# Create a new instance of the Edge driver
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

try:
    # Get the search query from the user
    search_query = input("Enter your search query: ")

    # Open Google's homepage
    driver.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Type in the search query
    search_box.send_keys(search_query)

    # Submit the search query
    search_box.send_keys(Keys.RETURN)

    # Wait for the results page to load and display the results
    time.sleep(5)  # Increase wait time if necessary

    # Print the title of the search results page
    print(driver.title)

finally:
    # Close the browser window, even on exceptions
    driver.quit()
