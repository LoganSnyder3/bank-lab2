<<<<<<< HEAD
=======
# Banking System - Lab 2
# By: Logan Snyder
# Date: 10/10/2025

# List of account names
account_names = ["john", "zach", "paul", "mary", "susan"]

#List of account balances
account_balances = [150, 200, 300, 100, 250]

#Main menu
>>>>>>> 018a8ab39677286ec791bcc457bc6c73d566f7be
check = False
while check == False:
    print("- Main Menu -")
    print("1. List all accounts")
    print("2. View an account balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Add account")
    print("7. Remove account")
<<<<<<< HEAD
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
    elif option == "5":
        input("Enter your account name: ")
    
        
        
    elif option == "9":
        check = True
=======
    print("8. Quit")

    option = input("Choose an option (1-8): ")

# List all acounts
    if option == "1":
        print(" - All Accounts -")
        for i in range(len(account_names)):
            print(f"{account_names[i]}")

# View all account balance  
    elif option == "2":
        name = input("Enter account name: ")
        if name in account_names:
            index = account_names.index(name)
            print("Balance for", name, "is $", account_balances[index])
        else:
            print("Account not found.")

# Deposit
    elif option == "3":
        name = input("Enter account name: ")
        if name in account_names:
            index = account_names.index(name)
            amount = int(input("Enter amount to deposit: "))
            account_balances[index] = account_balances[index] + amount
            print(f"New balance for {name} is ${account_balances[index]}")
        else:
            print("Account not found.")
# Withdraw
    elif option == "4":
        name = input("Enter account name: ")
        if name in account_names:
            index = account_names.index(name)
            amount = int(input("Enter amount to withdraw "))
            if amount <= account_balances[index]:
                account_balances[index] = account_balances[index] - amount
                print(f"New balance for {name} is ${account_balances[index]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

# Transfer
    elif option == "5":
        from_name = input("Enter account to transfer from: ")
        to_name = input("Enter account to transfer to: ")
        if from_name in account_names and to_name in account_names:
            from_index = account_names.index(from_name)
            to_index = account_names.index(to_name)
            amount = int(input("Enter amount to transfer: "))
            if amount <= account_balances[from_index]:
                account_balances[from_index] = account_balances[from_index] - amount
                account_balances[to_index] = account_balances[to_index] + amount
                print(f"Transferred ${amount} from {from_name} to {to_name}")
                print(f"{from_name}'s new balance is ${account_balances[from_index]}")
                print(f"{to_name}'s new balance is ${account_balances[to_index]}")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts not found.")

# Add account
    elif option == "6":
        name = input("Enter new account name: ")
        if name in account_names:
            print("Account already exists.")
        else:
            balance = int(input("Enter starting balance: "))
            account_names.append(name)
            account_balances.append(balance)
            print(f"Account '{name}' added with ${balance}")
            print("Updated Account List: ")
            for i in range(len(account_names)):
                print(f"{account_names[i]} : ${account_balances[i]}")
            

# Remove account
    elif option == "7":
        name = input("Enter account name to remove: ")
        if name in account_names:
            index = account_names.index(name)
            account_names.pop(index)
            account_balances.pop(index)
            print(f"Account '{name}' has been removed.")
            print("Updated Account List: ")
            for i in range(len(account_names)):
                print(f"{account_names[i]} : ${account_balances[i]}")
        else:
            print("Account not found.")

# Quit option
    elif option == "8":
        print("Goodbye.")
        check = True

    else:
        print("Invalid option. Please choose a number from 1 to 8.")
>>>>>>> 018a8ab39677286ec791bcc457bc6c73d566f7be
