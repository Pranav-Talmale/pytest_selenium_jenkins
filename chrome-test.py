from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set path to Brave browser
brave_path = "/usr/share/applications/brave-browser.desktop"

# Set up ChromeOptions for Brave
options = Options()
options.binary_location = brave_path

# Initialize driver (chromedriver must be in PATH or specified)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://www.google.com/")

# Locate the search box, type search term, and press Enter
search_box = driver.find_element("name", "q")
time.sleep(20)
search_box.send_keys("Pranav Talmale")
time.sleep(20)
search_box.send_keys(Keys.ENTER)

input("Press Enter to close the browser...")
driver.quit()