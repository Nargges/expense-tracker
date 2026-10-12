def show_menu():
    print("1: add an expense")
    print("2: show my expenses")
    print("3: show the total cost")
    print("0: Exit")

def show_total(expenses):
    s = 0
    for expense in expenses:
        s += expense["amount"]

    print(f"total: ", s)


def show_expenses(expenses):
    if len(expenses) == 0:
        print("Your list is empty!")
    else:
        for expense in expenses:
            print(expense["amount"], expense["category"], expense["description"])

def add_expense(expenses):
    amount = float(input("amount: "))   #چون در ادامه باید sum محاسبه کنیم
    category = input("category: ")
    description =  input("description: ")


    expense =  {"amount": amount, "category": category, "description": description}

    

    expenses.append(expense)
    print("Expense added!")   #the return line is not nedded

def main():
    expenses = []    #a big list which contains some dictionary 

    while True:
        show_menu()
        choice = input("your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "0":
            print("Bye")
            break
        
        else: 
            print("Invalid choice")


main()

    

             



