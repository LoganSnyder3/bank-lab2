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
    if account in ["john","zach","Paul","mary","susan"]:
        print(f"{account}'s balance is $1000")
    else:
        print("Account not found.")
