"""

"""

import pprint

customer_balances = {}

with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, account_balance = line.strip().split("|")
        customer_balances[account_number] = float(account_balance)
        print()
        
pprint.pp(customer_balances)

#     for account_number, account_balance in content:
#     customer_balances = 

# file = open("account_balances.txt", r)
# content = file.read().split("|")

# print(type(customer_balances))

