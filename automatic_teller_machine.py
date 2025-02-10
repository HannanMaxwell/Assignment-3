""" 

"""

import random

menu_options = ("D", "W", "Q")
bank_balance = random.randint(-1000,10000)
asterisks = "*"
width = 40


print(asterisks * width)
print("PIXELL RIVER FINANCIAL".center(width))
print("ATM Simulator\n".center(width))
print(f"Your current balance is: ${bank_balance:,.2f}\n".center(width))
print(f"Deposit: {menu_options[0]}".center(width))
print(f"Withdraw: {menu_options[1]}".center(width))
print(f"Quit: {menu_options[2]}".center(width))
print(asterisks * width)


