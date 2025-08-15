import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="book_collection",
    user="postgres",
    password="10172006"
)
cursor = conn.cursor()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    year = input("Enter year published: ")
    cursor.execute(
        "INSERT INTO public.books (title, author, genre, year) VALUES (%s, %s, %s, %s)",
        (title, author, genre, year)
    )
    conn.commit()
    print("Book added successfully.")

def remove_book():
    book_id = input("Enter the book ID to remove: ")
    cursor.execute("DELETE FROM public.books WHERE id = %s", (book_id,))
    conn.commit()
    print("Book removed if it existed.")

def list_books():
    cursor.execute("SELECT * FROM public.books ORDER BY id")
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")

def main_menu():
    while True:
        print("\nBook Collection Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. List all books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            list_books()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

cursor.close()
conn.close()
