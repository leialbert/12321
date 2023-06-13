import psycopg2
from psycopg2.extras import execute_values

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname="v12321",
    user="albert",
    password="Lei.110120",
    host="127.0.0.1"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# # Create table if it doesn't exist
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS phone_numbers (
#         number VARCHAR(11) PRIMARY KEY
#     )
# """)

# # Commit the transaction
# conn.commit()

unique_substrings = set()

with open('WuRaoHaoMa20.txt', 'r') as f:
    for line in f:
        # Get the last 11 characters of the line
        substring = line.strip()[-11:]
        # Add to the set (this automatically removes duplicates)
        unique_substrings.add(substring)

# Convert the set to a list of tuples for execute_values
unique_substrings = [(number,) for number in unique_substrings]

# Insert the unique substrings into the database
execute_values(cur, """
    INSERT INTO phone_phonenumber (number)
    VALUES %s
    ON CONFLICT DO NOTHING
""", unique_substrings)

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
