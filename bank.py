print("- Main Menu -")
print("1. List all accounts")
print("2. View an account balance")
print("3. Deposit")
print("4. Withdraw")
print("5. Transfer")
print("6. Add account")
print("7. Remove account")
print("8. Save accounts to file")
print("9. Quit")
option = input("Choose an option (1-9): ")
if option == '1':
    print("john","zach","Paul","mary","susan")
elif option == '2':
    account = input("Enter account name: ")
    if account == "john":
        print("Balance for john: $150.50")
    elif account == "zach":
        print("Balance for zach: $200.75")
    elif account == "Paul":
        print("Balance for Paul: $300.00")
    elif account == "mary":
        print("Balance for mary: $100.25")
    elif account == "susan":
        print("Balance for susan: $250.00")
    else:
        print("Account not found.")
elif option == '3':
    account = input("Enter account name: ")
    balance = input("Enter amount to deposit: ")
    balance = int(balance)
    if account == "john":
        sum = 150.50 + balance
        print("New balance for john: $", sum)
    elif account == "zach":
        sum = 200.75 + balance
        print("New balance for zach: $", sum)
    elif account == "Paul":
        sum = 300.00 + balance
        print("New balance for Paul: $", sum)
    elif account == "mary":
        sum = 100.25 + balance
        print("New balance for mary: $", sum)
    elif account == "susan":
        sum = 250.00 + balance
        print("New balance for susan: $", sum)
    else:
        print("Account not found.")
elif option == '4':
    account = input("Enter account name: ")
    balance = input("Enter amount to withdraw: ")
    balance = int(balance)
    if account == "john":
        difference = 150.50 - balance
        print("New balance for john: $", difference)
    elif account == "zach":
        difference = 200.75 - balance
        print("New balance for zach: $", difference)
    elif account == "Paul":
        difference = 300.00 - balance
        print("New balance for Paul: $", difference)
    elif account == "mary":
        difference = 100.25 - balance
        print("New balance for mary: $", difference)
    elif account == "susan":
        difference = 250.00 - balance
        print("New balance for susan: $", difference)
    else:
        print("Account not found.")
elif option == '5':
        
        
    