import psycopg2
import pandas as pd

# Connect to your database
conn = psycopg2.connect(
    host="localhost",
    database="book_collection",
    user="postgres",          # admin user
    password="10172006",  # enter the password
)

cur = conn.cursor()

# Add a book
cur.execute(
    "INSERT INTO books (title, author, genre, year) VALUES (%s, %s, %s, %s)",
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
)

conn.commit()
    
# Retrieve books and print as table
cur.execute("SELECT * FROM books;")
rows = cur.fetchall()
df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
print(df)
    
cur.close()
conn.close()
