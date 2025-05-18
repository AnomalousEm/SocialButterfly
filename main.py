'''
SOCIAL BUTTERFLY - Main
Description: SocialButterfly is a social media scheduling application with the 
goal of reducing time to create and post content.
Author: Emily Shader
Date: 12/25/2024
'''

# Import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Information Gathering

# ISSA PORTAL DATA SCRAPER

# Create instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to ISSA Memeber Portal Login
driver.get("https://www.members.issa.org/login.aspx")

# Give time to load
time.sleep(5)

# Find and fill username/password
username_field = driver.find_element(By.NAME, "u")  # or ID/XPATH/CSS_SELECTOR
password_field = driver.find_element(By.NAME, "p")

username_field.send_keys("test")
password_field.send_keys("yrobot1234")

# output the full-page HTML
print(driver.page_source)

# Close browser instance
driver.quit()

# EVENTBRITE
# Get Events
# Schedule email campaign

# LINKEDIN COMPANY
# Post

# DISCORD
# Post

# TWITTER/X
# Post
# INSTAGRAM
# Post


# Application startup actions
# GUI objects, call methods, etc.