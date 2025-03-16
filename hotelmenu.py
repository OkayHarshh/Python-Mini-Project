# Hotel Menu using Dictionary
menu = {
    'Pizza': 250,
    'Burger': 150,
    'Pasta': 100,
    'French fries': 50,
    'Sandwich': 100,
    'Chicken': 200,
    'Noodles': 150,
    'Ice cream': 50,
    'Cake': 100,
    'Soft drink': 50
}

# Convert menu keys to a format that removes spaces & makes it lowercase
menu_normalized = {item.lower().replace(" ", ""): price for item, price in menu.items()}

# Greeting customer
print("\nWelcome to Our Hotel! 🍽️")
print("\nHere is our menu:\n")

for item, price in menu.items():
    print(f"{item}: Rs {price}")

print("\nLet's take your order!\n")

# Initialize order total
orderTotal = 0

# Function to get valid item from the user
def get_valid_item():
    while True:
        item = input("Enter the item you want to order: ").strip().lower().replace(" ", "")
        if item in menu_normalized:
            return item
        else:
            print("Item not available! Please enter a valid item.\n")

# Get first valid item
item1 = get_valid_item()
orderTotal += menu_normalized[item1]
print(f"{item1} added to your order.\n")

# Keep asking if the user wants more items
while True:
    anotherItem = input("Do you want to order another item? (yes/no): ").strip().lower()

    if anotherItem == 'no':
        break  # Exit the loop if the user says no

    elif anotherItem == 'yes':
        item2 = get_valid_item()
        orderTotal += menu_normalized[item2]
        print(f"{item2} added to your order.\n")

    else:
        print("Please enter 'yes' or 'no'.\n")  # Handles invalid inputs

# Display the total order amount
print(f"\nThank you for your order! 🍕🍔🍜\nYour total amount is: Rs {orderTotal}\n")
