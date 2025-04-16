'''
SOCIAL BUTTERFLY - Main
Description: SocialButterfly is a social media scheduling application with the 
goal of reducing time to create and post content.
Author: Emily Shader
Date: 12/25/2024
'''

# Import required modules
import sqlite3
import eventbrite
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Information Gathering

# ISSA PORTAL DATA SCRAPER

# Create instance of Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to ISSA Memeber Portal Login
driver.get("https://www.members.issa.org/login.aspx")

# Confirm title contains Python
assert "Python" in driver.title

input_element = driver.get_element(By.CLASS_NAME,"")

# Sleep for 10 seconds
time.sleep(10)

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