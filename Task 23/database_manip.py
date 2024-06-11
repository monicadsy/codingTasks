#   Import Libraries
import sqlite3

#   Declare Functions
def read_python_programming(file_name):
    python_programming = []

# Open and read the input file
    with open(file_name, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')
            # Convert employee number to integer
            id = int(fields[0])
            # Extract other fields
            name = fields[1]
            grade = int(fields[2])
            # Append the data to the python_programming list as a tuple
            python_programming.append((id, name, grade))

    return python_programming

# ==========  MAIN LOGIC - Database Manipulation with sqlite3  =============

db = sqlite3.connect('python_programming_db')

# Create a table called python_programming
cursor = db.cursor() # Get a cursor object

cursor.execute('''CREATE TABLE IF NOT EXISTS python_programmings (
                    id INTEGER, 
                    name TEXT NOT NULL, 
                    grade INTEGER)''')
db.commit()

# Call the function to read data from the file
python_programming_ = read_python_programming("python_programming.txt")

 # Insert the following new rows into the python_programming
cursor.executemany('''INSERT OR REPLACE INTO python_programmings (id, name, grade)
                        VALUES (?, ?, ?)''', python_programming_)

 # ====== Select all records with a grade between 60 and 80.
cursor.execute('''SELECT * FROM python_programmings 
                        WHERE grade BETWEEN ? AND ?''', (60, 80))

# ====== Change Carl Davis’s grade to 65.
cursor.execute('''UPDATE python_programmings SET id = ? 
                   WHERE name = ? AND grade = ?''', (55, 'Carl Davis', '65'))
db.commit()

# ====== Delete Dennis Fredrickson' row.
# Execute the SELECT statement to check if records exist
cursor.execute('''SELECT * FROM python_programmings WHERE id = ? ''', (66,))

# Check if the cursor is empty
if not cursor.fetchall():
    print("No records found. No action taken.")
else:
# Execute the DELETE statement to delete records
    cursor.execute('''DELETE FROM python_programmings WHERE id = ? ''', (66,))
    print("Records deleted successfully.")
    db.commit()

# Change the grade of all students with an id greater than 55 to a garde of 80
cursor.execute('''UPDATE python_programmings SET grade = ? 
                   WHERE id > ? ''', ('80', 55))
db.commit()

# print the table
for row in cursor:
        print(f"id: {row[0]}, name: {row[1]}, grade: {row[2]}")
       