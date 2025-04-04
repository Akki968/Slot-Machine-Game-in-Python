import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:] # [:] this symbol copies the elements of the
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns):
                print(columns[row], end = " | ")
            else:
                print(columns[row], end = "")
        print()


def deposit():
    while True:
        amount = input("Enter a amount to deposit: $")
        if amount.isdigit():  # isdigit() makes sure the input is a whole number
            amount = int(amount) 
            if amount >= 5:
                break
            else:
                print("Minimum amount to be deposited is $5.")
        else:
            print("Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the total number of lines to bet on (1 - {MAX_LINES})?: ")
        if lines.isdigit():  # isdigit() makes sure the input is a whole number
            lines = int(lines) 
            if  1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the number of lines in the given range.")
        else:
            print("Please enter a valid amount.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line?: ")
        if amount.isdigit():  # isdigit() makes sure the input is a whole number
            amount = int(amount) 
            if  MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter the number between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:                                                 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough amount to bet, your current balance is {balance}")
        else:
            break
        
    print(f"You are betting {bet} on {lines} lines. Your Total bet is {total_bet}")
        
main()

slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
print_slot_machine(slots)