print("Welcome to the bank")
print("1. View Balance")
print("2. Deposit")
print("3. Withdraw")
option = input("Choose an option: ")
students = ["john","zach","Paul","mary","susan"]
balances = [100.50,200.75,50.25,300.00,150.00]
for i in range(len(students)):
    print(f"Student: {students[i]} Balance: {balances[i]}")