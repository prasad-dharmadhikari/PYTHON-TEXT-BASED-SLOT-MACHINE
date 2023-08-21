def deposit():
    while True:
        amount = input("What would you like to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than zero.")
        else:
            print("Please enter a number")
    return amount

deposit()