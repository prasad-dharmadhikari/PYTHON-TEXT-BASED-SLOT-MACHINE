MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines
    
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")
        else:
            print("Please enter a number")
    return amount
        

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(f"You are betting {bet} Rs on {lines} lines. Total bet is Rs.{bet * lines}")
main()