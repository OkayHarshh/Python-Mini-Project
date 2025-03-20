# Empty Dictionary to store contacts
contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create a new contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Search for a contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        # Create a new contact
        name = input("Enter the name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            contacts[name] = {"phone": phone, "email": email}
            print("Contact added successfully.")

    elif choice == 2:
        # View all contacts
        if not contacts:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for name, contact in contacts.items():
                print(f"{name}: Phone: {contact['phone']}, Email: {contact['email']}")

    elif choice == 3:
        # Update a contact
        name = input("Enter the name to update: ")
        if name in contacts:
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            contacts[name] = {"phone": phone, "email": email}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        # Delete a contact
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        # Search for a contact
        name = input("Enter the name to search: ")
        if name in contacts:
            print(f"{name}: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    elif choice == 6:
        # Exit the app
        print("Thank you for using our Contact Book App!")
        break

    else:
        print("Invalid choice. Please try again.")

    

