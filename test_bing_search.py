import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    # Set path to Brave browser
    brave_path = "/usr/share/applications/brave-browser.desktop" 

    # Set up options for Brave
    options = Options()
    options.binary_location = brave_path
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_bing_search(driver):
    # Navigate to Bing
    driver.get("https://www.bing.com/")
    time.sleep(2)

    # Find the search box and perform search
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Pranav Talmale")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    # Assert search term is in results page
    assert "Pranav Talmale" in driver.page_source