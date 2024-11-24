# Social Butterfly

# Import require modules
import sqlite3

# Connecting to sqlite
# Connection object
connection_obj = sqlite3.connect('issa.db')

# Create cursor object
cursor_obj = connection_obj.cursor()

# Create the POST table if it doesn't already exist
postTable = '''CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY,
            title TEXT
            platform TEXT
            associated_event TEXT
            associated_event_type TEXT
            post_date
            post_time
            )'''

cursor_obj.execute(postTable)
result = cursor_obj.fetchall()
print('SQLite Version is {}'.format(result))
print("postTable is ready.")

# Close the connection
connection_obj.close()