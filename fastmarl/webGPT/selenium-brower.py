from selenium import webdriver
import time

# Create an instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage you want to refresh
driver.get("https://chat.openai.com/")

while True:
    # Wait for 10 seconds
    time.sleep(30)
    
    # Refresh the webpage
    #driver.refresh()