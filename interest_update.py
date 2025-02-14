"""

"""

from pprint import pprint

customer_balances = {}

with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, account_balance = line.strip().split("|")
        customer_balances[account_number] = float(account_balance)

pprint(customer_balances)

for account_number, account_balance in customer_balances.items():
    if account_balance < 1000 and account_balance >= 0:
        customer_balances[account_number] = account_balance + (account_balance * 0.01)/12
    elif account_balance > 1000 and account_balance < 5000:
        customer_balances[account_number] = account_balance + (account_balance * 0.025)/12
    elif account_balance > 5000:
        customer_balances[account_number] = account_balance + (account_balance * 0.05)/12
    else:
        customer_balances[account_number] = account_balance + (account_balance * 0.1)/12


pprint(customer_balances)

with open("updated_balances_MR.csv", "w") as file:
    file.write("Account,Balance\n")
    for account_number, account_balance in customer_balances.items():
        file.write(f"{account_number}, {account_balance:.2f}\n")






