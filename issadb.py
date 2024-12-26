# SOCIAL BUTTERFLY
# Description: SocialButterfly is a social media scheduling application with the goal of reducing time to create and post content.
# Author: Emily Shader
# Date: 12/25/2024

# Import required modules
import sqlite3

# Connecting to sqlite by establishing connection object
connection_obj = sqlite3.connect('issa.db')

# Create cursor object
cursor_obj = connection_obj.cursor()

result = cursor_obj.fetchall()
print('SQLite Version is {}'.format(result))

# COMMUNICATIONS
# Create the communications table if it doesn't already exist
communicationsTable = '''CREATE TABLE IF NOT EXISTS communications (
            commid INTEGER PRIMARY KEY,
            platform TEXT
            createddate 
            createdtime
            creator TEXT
            )'''

cursor_obj.execute(communicationsTable)
print("communicationsTable is ready.")

# EVENTS
# Create the events table if it doesn't already exist
eventsTable = '''CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(eventsTable)
print("eventsTable is ready.")

# EVENTCOMMS
# Create the eventcomms table if it doesn't already exist
eventCommsTable = '''CREATE TABLE IF NOT EXISTS eventcomms (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(eventCommsTable)
print("eventCommsTable is ready.")

# EMAIL
# Create the email table if it doesn't already exist
emailTable = '''CREATE TABLE IF NOT EXISTS email (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(emailTable)
print("emailTable is ready.")

# DISCORD
# Create the discord table if it doesn't already exist
discordTable = '''CREATE TABLE IF NOT EXISTS discord (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(discordTable)
print("discordTable is ready.")

# TWITTER
# Create the twitter table if it doesn't already exist
twitterTable = '''CREATE TABLE IF NOT EXISTS twitter (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(twitterTable)
print("twitterTable is ready.")

# LINKEDIN
# Create the linkedin table if it doesn't already exist
linkedInTable = '''CREATE TABLE IF NOT EXISTS linkedin (
            id INTEGER PRIMARY KEY
            )'''

cursor_obj.execute(linkedInTable)
print("linkedInTable is ready.")

# Close the connection
connection_obj.close()