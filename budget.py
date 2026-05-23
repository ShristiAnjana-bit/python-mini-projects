import json
#line 1: Get the starting income and convert it to a decimal number(float)
income = float(input("Enter your monthly income:"))

#line 2: create an empty dictionary(like a java hashmap) to store "expense Name" :Amount
#expenses = {} REPLACEING this with
#Try to open and read the existing file
try:
    with open("expenses.json","r") as file: #'r' means read mode
         expenses = json.load(file) #load the json data back into a dictionary
    print("Loaded your saved expenses successfully!")
except FileNotFoundError:
    #if the file doesn't exist yet,that's fine!Just start with empty dictionary:
    print("No saved data found.Starting a fresh budget.")
    expenses ={}

#line 3: start an infinite loop that keep asking for expenses
while True:

    #Line 4: Ask for the name of the expenses first
    name = input("Enter expense name(or type 'done' to finish):")

    #line 5:check if the user wants to stop. we use .lower() so 'Done' also works.
    if name.lower() == 'done' :
        break #line 6: this exits the loop immediately

    #line 7: if they didn't type 'done' , ask for the cost of that specific expense
    amount = float(input(f"Enter amount for {name}:"))

#line 8: add the name and amount into our dictionary
    expenses[name] = amount

#line 9: print a clean header
print("\n--- Monthly Summary ---")

#line 10: loop through the dictionary to print every expense the user entered
for name, amount in expenses.items():
    print(f"{name}: ${amount}")

#line 11: calculate total expenses
#expenses.value() extracts just the number from our dictionary as sum() can add them up
total_expenses = sum(expenses.values())

#line 12: calculate remaining money
balance = income - total_expenses

#line 13: print the final financial breakdown
print("------------------------")
print(f"Total Income:   ${income}")
print(f"Total Expenses: ${total_expenses}")
print(f"Net Savings:    ${balance}")

#'with open' safely open a file and automatically closes it when done
#'w' stand for write done
with open ("expenses.json","w") as file:
    #this takes your 'expenses' dictionary and write it cleanly into the file
    json.dump(expenses,file, indent=4)
print("\n Data successfully saved to expenses.json!")
    
    