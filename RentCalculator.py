# Rent Calculator 

# Inputs we need from the user
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity units consumed = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

# Calculate total electricity bill
total_bill = electricity_spend * charge_per_unit

# Calculate amount per person
output = (food + rent + total_bill) // persons

# Output result
print("Total electricity bill =", total_bill)
print("Total amount you've to pay is =", output)
