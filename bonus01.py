def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Balansda mablag' yetarli emas!")
        return balance

def check_balance(balance):
    print("Joriy balans:", balance)

balance = 1000.0

action = input("Amalni kiriting (deposit, withdraw, check): ")

if action == "deposit":
    amount = float(input("Summani kiriting: "))
    balance = deposit(balance, amount)
    check_balance(balance)

elif action == "withdraw":
    amount = float(input("Summani kiriting: "))
    balance = withdraw(balance, amount)
    check_balance(balance)

elif action == "check":
    check_balance(balance)

else:
    print("Noto'g'ri amal!")