from database_connection import connect_database
conn = connect_database()
cursor = conn.cursor()

def add_user():
    name=input("Please introduce the user name")
    try:
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (name,))
        conn.commit()
        print("User correctly added")
        return cursor.lastrowid
        
    except Exception as e:
        print(f"Error adding usser: {e}")
        conn.rollback() 
        return None
    



def view_user():
    name = input("Please introduce the user name: ")
    try:
        query = """
        SELECT id, name
        FROM users 
        WHERE name = %s
        """
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        users = []
        for row in results:
            user = {
                'id': row[0],
                'name': row[1],
            }
            users.append(user)
        print(users)     
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def display_all_users():
    try:
        query = """
        SELECT id, name
        FROM users
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No users found.")

        users = []
        for row in results:
            user = {
                'id': row[0],
                'name': row[1],
            }
            users.append(user)

        print("Authors found:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}")
        
        print(users)
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()




def user_operations():
    user_input = input('''User Operations:

                        1. Add a new user
                        2. View user details
                        3. Display all users
                        
                        Choose an option: ''')
    if user_input == "1":
        add_user()
    elif user_input == "2":
        view_user()
    elif user_input == "3":
        display_all_users()
    else:
        print("Invalid option. Please try again.\n")
