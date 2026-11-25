import os
from datetime import datetime

class JournalManager:
    def add_entry(self):
        entry = input("Enter entry: ")
        try:
            with open("journal.txt", "a") as f:
                date = datetime.now()
                f.write(str(date) + "\n")
                f.write(entry + "\n")
                f.write("--------------------\n")
            print("Entry added successfully!")
        except PermissionError:
            print("Permission denied!")

    # Method to display 
    def view_entries(self):
        try:
            with open("journal.txt", "r") as f:
                print("\nAll Journal Entries:")
                print(f.read())

        except FileNotFoundError:
            print("Journal file does not exist!")
        except PermissionError:
            print("Permission denied!")

    # Method to search for a journal entry
    def search_entry(self):
        search = input("Enter keyword or date to search: ")
        try:
            with open("journal.txt", "r") as f:
                found = False

                # Read file line by line
                for line in f:
                    if search.lower() in line.lower():
                        print(line, end="")
                        found = True
                if found == False:
                    print("Entry not found!")  
        except FileNotFoundError:
            print("Journal file does not exist!")
        except PermissionError:
            print("Permission denied!")


# Method to delete all journal entries
    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            try:               
                with open("journal.txt", "r+") as f:             
                    f.seek(0)
                    f.truncate()
                print("All entries deleted successfully!")
            except FileNotFoundError:
                print("Journal file does not exist!")
            except PermissionError:
                print("Permission denied!")
        else:
            print("Delete cancelled!")

# Create an object of JournalManager class
j = JournalManager()

while True:   
    print("\nWelcome to Personal Journal Manager!")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        j.add_entry()
    elif choice == "2":
        j.view_entries()
    elif choice == "3":
        j.search_entry()
    elif choice == "4":
        j.delete_entries()
    elif choice == "5":
        print("Thank you for using Personal Journal Manager!")
        break
    else:
        print("Invalid choice! Please try again.")
