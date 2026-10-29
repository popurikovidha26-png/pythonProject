balance = 5000
withdrawal_limit = 2000
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. Deposit  2. Withdraw")
    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif choice == 1:
        balance += amount
        transactions.append("Deposit: " + str(amount))
        print("Deposit successful")
    elif choice == 2:
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append("Withdraw: " + str(amount))
            print("Withdrawal successful")
    else:
        print("Invalid transaction")

print("\nTransaction Summary")
for t in transactions:
    print(t)

print("Final Balance:", balance)
