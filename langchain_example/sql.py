# Import sqlite3 module
import sqlite3

# Connect to the database file
conn = sqlite3.connect("Chinook.db")

# Create a cursor object
cursor = conn.cursor()

# Execute a query to get the names of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch the results as a list of tuples
tables = cursor.fetchall()

# Print the list of tables
print("The tables in the database are:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
