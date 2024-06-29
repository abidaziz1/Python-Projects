from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def login_to_twitter(username, password):
    # Path to the ChromeDriver executable
    driver_path = r"F:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Optional: Maximize the browser window

    # Initialize Chrome WebDriver with options
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    try:
        # Your login automation code here
        # Open Twitter login page
        driver.get("https://twitter.com/login")

        # Find username input field and enter username
        username_field = driver.find_element_by_name("session[username_or_email]")
        username_field.send_keys(username)

        # Find password input field and enter password
        password_field = driver.find_element_by_name("session[password]")
        password_field.send_keys(password)
        password_field.submit()

        # Wait for the login process to complete
        driver.implicitly_wait(10)  # Adjust this if needed

        # Verify if login was successful
        if "twitter.com/home" in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed. Please check your credentials.")

    finally:
        # Ensure to quit the WebDriver session
        driver.quit()

if __name__ == "__main__":
    # Replace with your Twitter username and password
    twitter_username = "your_twitter_username"
    twitter_password = "your_twitter_password"

    # Call the function to login
    login_to_twitter(twitter_username, twitter_password)
