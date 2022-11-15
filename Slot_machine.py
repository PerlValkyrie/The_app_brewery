# Follow along project by Tech with Tim https://www.youtube.com/watch?v=th4OBktqK1I

# Incomplete; stopped at 16 minutes. Some confusion with the amount and lines variables

MAX_LINES = 3    # Constant value
MAX_BET = 100
MIN_BET = 1


# Ask to enter a deposit
def deposit():
    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")$ ")
        if lines.isdigit():    # ensure it's a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:      # ensure is valid amount
                break           # ends while look
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        lines = input("What would you like to bet on each line? $")
        if lines.isdigit():    # ensure it's a number
            lines = int(lines)
            if MIN_BET <= lines <= MAX_BET:      # ensure is valid amount
                break           # ends while look
            else:
                print("Amount must be between.")
        else:
            print("Please enter a number.")
    return lines

def get_number_of_lines():



    def main():
        balance = deposit()
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
        print(balance, lines)



        main()

