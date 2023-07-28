# db_migrate.py



#------------------------------------------------------------------------------------------------
# Database Migration Script
#------------------------------------------------------------------------------------------------
# This script is used to migrate the data from an existing table to a new table with an additional "column3".
# It performs the following steps:
# 1. Connects to the database using SQLite3.
# 2. Renames the existing table to "old_table".
# 3. Creates a new table using SQLAlchemy with an additional "column3".
# 4. Retrieves data from "old_table" and adds "column3" with a default value.
# 5. Inserts the modified data into the new table.
# 6. Drops the "old_table" after the migration is complete.

####################################
### Import the necessary modules ###
####################################

import sqlite3
from project import db, app
from project._config import DATABASE_PATH

# Connect to the database
with sqlite3.connect(DATABASE_PATH) as connection:
    # Create a cursor object
    c = connection.cursor()

    # Step 1: Rename the existing table to "old_table"
    c.execute("ALTER TABLE table RENAME TO old_table")

    # Step 2: Create the new table using SQLAlchemy
    with app.app_context():
        db.create_all()

    # Step 3: Retrieve data from "old_table" and add "column3" with a default value
    c.execute("SELECT column1, column2 FROM old_table ORDER BY column1 ASC")
    data = [(row[0], row[1], "column3") for row in c.fetchall()]

    # Step 4: Insert the modified data into the new table
    c.executemany("INSERT INTO table (column1, column2, column3) VALUES (?, ?, ?)", data)

    # Step 5: Drop the "old_table" after the migration is complete
    c.execute("DROP TABLE old_table")
