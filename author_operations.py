from database_connection import connect_database
conn = connect_database()
cursor = conn.cursor()

def add_author():
    name=input("Please introduce the user name")
    biography=input("Please introduce the biography")
    try:
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (name, biography))
        conn.commit()
        print("Author correctly added")
        return cursor.lastrowid
        
    except Exception as e:
        print(f"Error adding usser: {e}")
        conn.rollback() 
        return None



def view_author():
    name = input("Please introduce the author name: ")
    try:
        query = """
        SELECT id, name, biography
        FROM authors 
        WHERE name = %s
        """
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        authors = []
        for row in results:
            author = {
                'id': row[0],
                'name': row[1],
                'biography': row[2],
            }
            authors.append(author)
        print(authors)     
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def display_all():
    try:
        query = """
        SELECT id, name, biography
        FROM authors
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No authors found.")

        authors = []
        for row in results:
            author = {
                'id': row[0],
                'name': row[1],
                'biography': row[2],
            }
            authors.append(author)

        print("Authors found:")
        for author in authors:
            print(f"ID: {author['id']}, Name: {author['name']}, Biography: {author['biography']}")
        
        print(authors)
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()






def author_operations():
    user_input=input('''Author Operations:

                        1. Add a new author
                        2. View author details
                        3. Display all authors''')
    if user_input=="1":
        add_author()
    elif user_input=="2":
        view_author()
    elif user_input=="3":
        display_all()




