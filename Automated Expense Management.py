# Expense Tracker Project 

expensesList = [] # list of expenses in form of dictionary 
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

# ADD Expense
    if(choice == 1):
        date = input("Enter the date of expense: ")
        category = input("Enter the category (Food, Travel, Makeup, Books): ")
        description = input("Enter brief description/details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n Expense added successfully!")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList) == 0 ):
            print("No expenses recorded yet. Please add an expense first.")
        else:
            print("===== Your Expense Records ======")
            count = 1
            for totalSpent in expensesList:
                print(f"Expense Number {count} -> {totalSpent['date']}, {totalSpent['category']}, {totalSpent['description']}, {totalSpent['amount']} ")
                count = count + 1

# 3. View Total Spending 
    elif(choice == 3):
        total = 0
        for totalSpent in expensesList:
            total = total + totalSpent["amount"]

        print("\n TOTAL EXPENSES = ", total)

# 4. EXIT 
    elif(choice == 4):
        print("Thank you for using our Application!")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")