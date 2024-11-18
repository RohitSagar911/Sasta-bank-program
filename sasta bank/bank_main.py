# Function to load balances from the file
def load_balances():
    balances = {}
    try:
        with open("balances.txt", "r") as file:
            for line in file:
                name, balance = line.strip().split(":")
                balances[name] = int(balance)
    except FileNotFoundError:
        # File does not exist yet, so we will create it when needed
        pass
    return balances

# Function to save balances to the file
def save_balances(balances):
    with open("balances.txt", "w") as file:
        for name, balance in balances.items():
            file.write(f"{name}:{balance}\n")

# Initialize balances from file
balances = load_balances()

# Main functions for banking operations
def show_balance(userName, balance):
    print(f"Mr.{userName}, your current balance is {balance}\n")
    return balance

def deposit(balance):
    try:
        amount = int(input("Enter the deposit amount: "))
        if amount < 0:
            print("Deposit amount must be positive. Try again.")
            return deposit(balance)
    except ValueError: #checking value error
        print("Amount should be in numbers only. Try again.")
        return deposit(balance)
    else:
        balance += amount
        print(f"\nTotal amount of {amount} has been credited to your bank account. Your current bank balance is {balance}\n")
    return balance

def withdraw(balance):
    try:
        amount = int(input("Enter the withdrawal amount: "))
        if amount < 0:
            print("Withdrawal amount must be positive. Try again.")
            return withdraw(balance)
    except ValueError:
        print("Amount should be in numbers only. Try again.")
        return withdraw(balance)
    else:
        if amount > balance:
            print("Withdrawal amount can't be greater than your bank balance. Try again.")
            return withdraw(balance)
        else:
            balance -= amount
            print(f"\nTotal amount of {amount} has been debited from your bank account. Your current bank balance is {balance}\n")
    return balance

# Start of the main program
is_running = True

print("\nWelcome to the Bank Program")
userName = input("Enter your name: ").capitalize() #capitalizes the user input 

# Check if the user already has a balance
balance = balances.get(userName, 0)

while is_running: 
    print("------------------------")
    print(f"Welcome Mr.{userName}")
    print("Please choose your banking program here:")
    print("-------------------------")
    print(" 1. Show balance")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Exit")
    
    choice = input("Enter your choice (1, 2, 3, 4): ")
    
    if choice == "1":
        show_balance(userName, balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        is_running = False
        balances[userName] = balance  # Update the balance in the dictionary
        save_balances(balances)  # Save all balances to the file
    else:
        print("\nInvalid entry, please try again\n")

print("Thank you for using the Bank Program. Goodbye!")

