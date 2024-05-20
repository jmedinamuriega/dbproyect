from database_connection import connect_database

conn = connect_database()
cursor = conn.cursor()

def add_book():
    title = input("Enter the book title: ")
    author_id = input("Enter the author ID: ")
    genre_id = input("Enter the genre ID: ")
    isbn = input("Enter the ISBN: ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")
    
    try:
        cursor.execute("""
            INSERT INTO books (title, author_id, genre_id, isbn, publication_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (title, author_id, genre_id, isbn, publication_date))
        conn.commit()
        print("Book added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")
        conn.rollback()

def borrow_book():
    book_id = input("Enter the book ID to borrow: ")
    
    try:
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        availability = cursor.fetchone()[0]
        
        if availability:
            cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
            conn.commit()
            print("Book borrowed successfully.")
        else:
            print("Book is not available.")
    except Exception as e:
        print(f"Error borrowing book: {e}")
        conn.rollback()

def return_book():
    book_id = input("Enter the book ID to return: ")
    
    try:
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        availability = cursor.fetchone()[0]
        
        if not availability:
            cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
            conn.commit()
            print("Book returned successfully.")
        else:
            print("Book is already available.")
    except Exception as e:
        print(f"Error returning book: {e}")
        conn.rollback()

def search_book():
    search_query = input("Enter the title or ISBN to search: ")
    
    try:
        cursor.execute("""
            SELECT id, title, author_id, genre_id, isbn, publication_date, availability
            FROM books
            WHERE title LIKE %s OR isbn = %s
        """, ('%' + search_query + '%', search_query))
        
        results = cursor.fetchall()
        
        if results:
            for row in results:
                availability = "Available" if row[6] else "Not Available"
                print(f"ID: {row[0]}, Title: {row[1]}, Author ID: {row[2]}, Genre ID: {row[3]}, ISBN: {row[4]}, Publication Date: {row[5]}, Availability: {availability}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error searching for book: {e}")

def display_all_books():
    try:
        cursor.execute("SELECT id, title, author_id, genre_id, isbn, publication_date, availability FROM books")
        results = cursor.fetchall()
        
        if results:
            for row in results:
                availability = "Available" if row[6] else "Not Available"
                print(f"ID: {row[0]}, Title: {row[1]}, Author ID: {row[2]}, Genre ID: {row[3]}, ISBN: {row[4]}, Publication Date: {row[5]}, Availability: {availability}")
        else:
            print("No books available.")
    except Exception as e:
        print(f"Error displaying books: {e}")

def book_operations():
    while True:
        user_input = input('''\nBook Operations:

                        1. Add a new book
                        2. Borrow a book
                        3. Return a book
                        4. Search for a book
                        5. Display all books
                        6. Exit
                        
                        Choose an option: ''')
        if user_input == "1":
            add_book()
        elif user_input == "2":
            borrow_book()
        elif user_input == "3":
            return_book()
        elif user_input == "4":
            search_book()
        elif user_input == "5":
            display_all_books()
        elif user_input == "6":
            break
        else:
            print("Invalid option. Please try again.\n")


