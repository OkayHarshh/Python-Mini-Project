import pandas as pd
import numpy as np
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)

# Load data with proper date parsing
try:
    df = pd.read_csv(FILE_NAME, parse_dates=["Date"], dayfirst=True)
    # Ensure the Date column is datetime type
    df['Date'] = pd.to_datetime(df['Date'])
except pd.errors.EmptyDataError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

def add_expense():
    global df
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
    
    category = input("Enter category (e.g., Food, Travel, Rent): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    desc = input("Enter description (optional): ")
    new_expense = pd.DataFrame([[date, category, amount, desc]], columns=df.columns)
    
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("Expense added successfully!\n")

def show_summary():
    print("\n📊 Total Expenses: ₹", df["Amount"].sum())
    print("\n📂 Category-wise Summary:")
    print(df.groupby("Category")["Amount"].sum().sort_values(ascending=False))

def show_monthly_summary():
    # Ensure Date column is datetime
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby('Month')['Amount'].sum()
    print("\n🗓️ Monthly Expense Summary:")
    print(monthly)

def main():
    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Show Monthly Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            show_monthly_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()