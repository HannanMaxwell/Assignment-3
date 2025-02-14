"""This program demonstrates the ability to read from files and write 
    to files. The program applies interest rates to the account
    balances and then creates a csv with updated balances.
"""

__author__ = "Muhammad Rahmani"
__version__ = "1.0.0"

# pprint is pretty print which prints the dictionaries in columns
# which makes the data more readabke.
# csv will be used to read from the csv file to print it to the console
from pprint import pprint
import csv

# customer_balances is a dictionary which holds account numbers and
# account balances. The account numbers are the keys and the account
# balances are the values.
customer_balances = {}

# We open the file account_balances.txt to read from it.
with open("account_balances.txt", "r") as file:
    # After opening the account_balances.txt file, we loop through
    # the file line by line and assign the key/account number to
    # account_number variable and account balance to account_balance
    # variable. Then the account_number and account_balance are added
    # to the customer_balances dictionary.
    for line in file:
        account_number, account_balance = line.strip().split("|")
        customer_balances[account_number] = float(account_balance)

# Pretty prints the customer_balances
pprint(customer_balances)

# This for loop loops through the customer_balances dictionary to check
# the account balances and applying interest rates based on what range
# the balance falls in between.
for account_number, account_balance in customer_balances.items():
    # If the account balance is less than 1000 and more than or equal to 
    # zero, then the account balance is applied an interest rate of 1%.
    if account_balance < 1000 and account_balance >= 0:
        customer_balances[account_number] = account_balance + (account_balance * 0.01)/12
    # If the account balance is greater than 1000 and less than 5000,
    # then an interest of 2.5% is applied to the account balance.
    elif account_balance > 1000 and account_balance < 5000:
        customer_balances[account_number] = account_balance + (account_balance * 0.025)/12
    # If the account balance is greater than 5000, then the account
    # balance is applied the interest rate of 5%.
    elif account_balance > 5000:
        customer_balances[account_number] = account_balance + (account_balance * 0.05)/12
    # If the account balance is negative, the account balance is
    # charged an interest of 10%.
    else:
        customer_balances[account_number] = account_balance + (account_balance * 0.1)/12

print("\n")
pprint(customer_balances)
print("\n")

# Creates updated_balances_MR.csv file. Then writes the
# updated balances from the customer_balances dictionary
# to the updated_balances_MR.csv file.
with open("updated_balances_MR.csv", "w") as file:
    file.write("Account,Balance\n")
    for account_number, account_balance in customer_balances.items():
        file.write(f"{account_number}, {account_balance:.2f}\n")

# Opens the updated_balances_MR.csv file, reads through
# it and then prints it to the console.
with open ("updated_balances_MR.csv", newline = "") as csvfile:
    accounts = csv.DictReader(csvfile)
    for row in accounts:
        print(row["Account"], row["Balance"])



