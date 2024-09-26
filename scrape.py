import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Path to your Chrome user data directory
user_data_dir = "C:\\Users\\LAW\\AppData\\Local\\Google\\Chrome\\User Data"  # Make sure this path is correct

# URL of the web page you want to scrape
url = "https://www.youtube.com"

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_data_dir}")

# Initialize Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# Open the web page
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

site = driver.find_element(By.TAG_NAME, "body")

scrollDown_count = 10
while scrollDown_count:
    site.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    scrollDown_count -= 1

    
# Get the page source after JavaScript execution
html = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Extract data
# Extracting video titles and links
videos = soup.find_all('a', id='video-title-link')
for video in videos:
    title = video.get('title')
    link = "https://www.youtube.com" + video.get('href')
    
    print(f"Title: {title}\nLink: {link}\n")

#TODO: add channel and upload date into scraped data as feature in code
#TODO: convert code into function getVideos() for reusing
#TODO: repeat with changed url for history

# Close the WebDriver
driver.quit()
