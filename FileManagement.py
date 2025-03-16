import os

def create_file(file_name):
    try:
        if os.path.exists(file_name):
            print(f'File {file_name} already exists')
        else:
            with open(file_name, 'x') as f:
                print(f'File {file_name} created successfully')
    except Exception as e:
        print(f'Error creating file: {e}')

def view_all_files():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if files:
        print('Files in the current directory:')
        for file in files:
            print(file)
    else:
        print('No files found in the current directory.')

def delete_file(file_name):
    try:
        if os.path.exists(file_name):
            confirm = input(f'Are you sure you want to delete {file_name}? (yes/no): ').strip().lower()
            if confirm == 'yes':
                os.remove(file_name)
                print(f'File {file_name} deleted successfully')
            else:
                print('File deletion cancelled.')
        else:
            print(f'File {file_name} not found')
    except Exception as e:
        print(f'Error deleting file: {e}')

def read_file(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                print(f'Content of {file_name}:\n')
                print(f.read())
        else:
            print(f'File {file_name} not found')
    except Exception as e:
        print(f'Error reading file: {e}')

def write_file(file_name):
    try:
        content = input('Enter the content to write: ')
        with open(file_name, 'w') as f:
            f.write(content)
        print(f'Content written to {file_name} successfully')
    except Exception as e:
        print(f'Error writing to file: {e}')

def append_file(file_name):
    try:
        content = input('Enter the content to append: ')
        with open(file_name, 'a') as f:
            f.write('\n' + content)
        print(f'Content appended to {file_name} successfully')
    except Exception as e:
        print(f'Error appending to file: {e}')

def file_management():
    print("Welcome to File Management System")
    while True:
        print("\nChoose an option:")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Write to a file")
        print("6. Append to a file")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            file_name = input("Enter the file name to create: ").strip()
            create_file(file_name)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            file_name = input("Enter the file name to delete: ").strip()
            delete_file(file_name)
        elif choice == "4":
            file_name = input("Enter the file name to read: ").strip()
            read_file(file_name)
        elif choice == "5":
            file_name = input("Enter the file name to write to: ").strip()
            write_file(file_name)
        elif choice == "6":
            file_name = input("Enter the file name to append to: ").strip()
            append_file(file_name)
        elif choice == "7":
            print("Thank you for using File Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    file_management()


