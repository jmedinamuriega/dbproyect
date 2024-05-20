from database_connection import connect_database
conn = connect_database()
cursor = conn.cursor()
from database_connection import connect_database

conn = connect_database()
cursor = conn.cursor()

def add_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    try:
        cursor.execute("INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)", (name, description, category))
        conn.commit()
        print("Genre added successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error adding genre: {e}")

def view_genre():
    genre_id = input("Enter genre ID: ")
    try:
        cursor.execute("SELECT * FROM genres WHERE id = %s", (genre_id,))
        genre = cursor.fetchone()
        if genre:
            print(f"ID: {genre[0]}")
            print(f"Name: {genre[1]}")
            print(f"Description: {genre[2]}")
            print(f"Category: {genre[3]}")
        else:
            print("Genre not found.")
    except Exception as e:
        print(f"Error viewing genre: {e}")

def display_all_genres():
    try:
        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()
        if genres:
            for genre in genres:
                print(f"ID: {genre[0]}, Name: {genre[1]}, Description: {genre[2]}, Category: {genre[3]}")
        else:
            print("No genres found.")
    except Exception as e:
        print(f"Error displaying genres: {e}")

def genre_operations():
    while True:
        user_input = input('''Genre Operations:

                        1. Add a new genre
                        2. View genre details
                        3. Display all genres
                        4. Exit
                        
                        Choose an option: ''')
        if user_input == "1":
            add_genre()
        elif user_input == "2":
            view_genre()
        elif user_input == "3":
            display_all_genres()
        elif user_input == "4":
            break
        else:
            print("Invalid option. Please try again.\n")

def genre_operations():
    user_input = input('''Genre Operations:

                        1. Add a new genre
                        2. View genre details
                        3. Display all genres
                        
                        Choose an option: ''')
    if user_input == "1":
        add_genre()
    elif user_input == "2":
        view_genre()
    elif user_input == "3":
        display_all_genres()
    else:
        print("Invalid option. Please try again.\n")
