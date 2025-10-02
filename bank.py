print("Welcome to the bank")
print("1. View Balance")
print("2. Deposit")
print("3. Withdraw")
option = input("Choose an option: ")
if option == "1":
    students = ["john","zach","Paul","mary","susan"]
balances = [100.50,200.75,50.25,300.00,150.00]
for i in range(len(students)):
    print(f"Student: {students[i]} Balance: {balances[i]}")
if option == "2":
    input("Enter your name: ")
    students = input()
    if students == ("john"):
        print("You currently have $100.50")
    input("How much would you like to deposit? ")
    add = input()
    if students == ("zach"):
        print("You currently have $200.75")
    input("How much would you like to deposit? ")
    add = input()
    if students == ("paul"):
        print("You currently have $50.25")
        input("How much would you like to deposit? ")
    add = input()
    if students == ("mary"):
        print("You currently have $300.00")
        input("How much would you like to deposit? ")
    add = input()
    if students == ("susan"):
        print("You currently have $150.00")
        input("How much would you like to deposit? ")
    add = input()
        
   
