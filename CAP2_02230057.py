##########################################################################################################
# Name: Chandra Bdr Ghalley
# Department: B.E First Year Electrical Engineering
# Student ID: 02230057
#####################################
#            References
#https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
#https://www.freecodecamp.org/news/how-to-build-an-online-banking-system-python-oop-tutorial/
#https://youtu.be/BRssQPHZMrc?si=Totx1cnORqDAFyVw
#https://youtu.be/xTh-ln2XhgU
#https://pythonmania.org/python-program-for-bank-account-using-class/
##########################################################################################################

import random # This imported random module provides functions for generating random numbers, selecting random elements from a sequence , range and more.

class Account:
    def __init__(self, account_number, password, account_type):
        self.account_number = account_number
        self.password = password 
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # Add the deposite amount to the balance
            print(f"Deposited Nu.{amount:.2f}. New balance: Nu.{self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount # It deduct the withdrawal amount from the balance
            print(f"Withdrew Nu.{amount:.2f}. New balance: Nu.{self.balance:.2f}")
        else:
            print("Insufficient amount.")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount # It detuct the transfer amount from the current amount balance
            target_account.balance += amount # It adds the transfer amount to the target amount balance
            print(f"Transferred Nu.{amount:.2f} to account {target_account.account_number}.")
        else:
            print("Insufficient amount.")

    def check_balance(self):
        print(f"Current balance: Nu.{self.balance:.2f}")# It displays the current balance

class Bank:
    def __init__(self):
        self.accounts = {}# It is dictonary to store the account information

    def create_account(self, account_type):
        account_number = str(random.randint(100000, 999999))# From this range it generates the random account number
        password = str(random.randint(1000, 9999))# From this range it generates the random password
        self.accounts[account_number] = Account(account_number, password, account_type) # It stores the new account information
        print(f"Account created. Account Number: {account_number}, Password: {password}")

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print("Login successful.")
            return account
        print("Incorrect account number or password.")
        return None
# This function helps to create the bank account
def main():
    bank = Bank() #Initialize a Banl object to manage accounts.

    while True: # This the main loop tokeep the program running until the user chooses to exit.
        choice = input("\n1. Open Account\n2. Login\n3. Exit\nEnter your choice: ") # It is the display for the user to get user choice.

        if choice == "1":
            account_type = input("Enter account type (P for Personal/ B for Business): ")
            if account_type in ["P", "B"]:
                bank.create_account(account_type)
            else:
                print("Invalid account type.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    user_choice = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout\nEnter your choice: ")
                    if user_choice == "1":
                        account.check_balance()
                    elif user_choice == "2":
                        account.deposit(float(input("Enter amount to deposit: ")))
                    elif user_choice == "3":
                        account.withdraw(float(input("Enter amount to withdraw: ")))
                    elif user_choice == "4":
                        target_account_number = input("Enter target account number: ")
                        target_account = bank.accounts.get(target_account_number)
                        if target_account:
                            account.transfer(float(input("Enter amount to transfer: ")), target_account)
                        else:
                            print("Target account does not exist.")
                    elif user_choice == "5":
                        print("Logged out successfully.")
                        break # This break function helps to break out of the loop which means to logout
                    else:
                        print("Invalid choice. Please select a valid option.")

        elif choice == "3":
            print("Exiting the application. Thank you!")
            break # This break funtion helps to exit the application
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main() # This is the main function which executes the code. 