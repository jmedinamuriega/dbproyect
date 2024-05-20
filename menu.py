from book_operations import book_operations
from author_operations import author_operations
from genre_operations import genre_operations
from user_operations import user_operations


def main():
    while True:
        try:
            user_selection = input(''' Main Menu:
                                    1. Book Operations
                                    2. User Operations
                                    3. Author Operations
                                    4. Genre Operations
                                    5. Quit
                                    Please enter your choice (1-5): ''')
            
            if user_selection == "1":
                try:
                    book_operations()
                except Exception as e:
                    print(f"An error occurred during Book Operations: {e}")
            elif user_selection == "2":
                try:
                    user_operations()
                except Exception as e:
                    print(f"An error occurred during User Operations: {e}")
            elif user_selection == "3":
                try:
                    author_operations()
                except Exception as e:
                    print(f"An error occurred during Author Operations: {e}")
            elif user_selection == "4":
                try:
                    genre_operations()
                except Exception as e:
                    print(f"An error occurred during Genre Operations: {e}")
            elif user_selection == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid selection. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()