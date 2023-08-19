import os
import datetime

# Get the directory of the script
script_directory = os.path.dirname(__file__)

print("Welcome to the Personal Diary System")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Delete an entry")
    print("4. Exit")

    input_choice = input()

    if input_choice == "1":
        # Add a new entry
        title = input("Enter the title of the entry: ")
        content = input("Enter the content of the entry: ")

        # Get the current date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Create a directory for entries if it doesn't exist
        entries_directory = os.path.join(script_directory, "entries")
        if not os.path.exists(entries_directory):
            os.mkdir(entries_directory)

        # Create a filename based on the sanitized title and date
        sanitized_title = title.replace(" ", "_").lower()
        entry_file_name = os.path.join(entries_directory, f"{sanitized_title}_{current_date}.txt")
        with open(entry_file_name, "w") as entry_file:
            entry_file.write(f"Title: {title}\n")
            entry_file.write(f"Date: {current_date}\n")
            entry_file.write(f"Content:\n{content}\n")
        print("Entry saved successfully!")

    elif input_choice == "2":
        # View all entries
        entries = os.listdir(entries_directory)
        if entries:
            print("List of entries:")
            for entry in entries:
                print(entry)
        else:
            print("No entries available.")

    elif input_choice == "3":
        # Delete an entry
        entries = os.listdir(entries_directory)
        if entries:
            print("Select an entry to delete:")
            for index, entry in enumerate(entries, start=1):
                print(f"{index}. {entry}")
            choice = int(input())
            if 1 <= choice <= len(entries):
                entry_to_delete = entries[choice - 1]
                os.remove(os.path.join(entries_directory, entry_to_delete))
                print(f"{entry_to_delete} has been deleted.")
            else:
                print("Invalid choice.")
        else:
            print("No entries available.")

    elif input_choice == "4":
        print("Exiting the Personal Diary System")
        break

    else:
        print("Invalid choice. Please select a valid option.")
