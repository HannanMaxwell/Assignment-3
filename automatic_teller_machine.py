""" 

"""

__author__ = "Muhammad Rahmani"
__version__ = "1.0.0"

# Importing random, time and os from the library. The random is needed
# to randomize bank_balance variable each time the program runs.
# time will be needed to pause the script for 3 seconds.
# os is needed to clear the screen. 
import random
import time
import os

# Here I have assigned variables different values.
# menu_options is the tuple that contains options such as D for deposit
# W for withdrawal and Q for quitting the selection menu loop.
# asterisks will be used a few times so I have assigned it to a variable
# called asterisks. 
# bank_balance variable is assigned a random value from -1000 to 10000 
# each time the program is started over again.
# width variable is assigned the of value 40.
# loop_active variable will be used for the while loop. It will
# hold the boolean value of True and it will be used to quit program
# and exit the loop.
menu_options = ("D", "W", "Q")
bank_balance = random.randint(-1000,10000)
asterisks = "*"
width = 40
loop_active = True

# This while loop will keep looping unless the user chooses to quit the 
# loop by entering q. The user is presented with a selection menu that
# will allow the user to deposit and withdraw money from his account.
# The user has the option to deposit or withdraw money from his bacnk_balance,
# this is done using if statements. The user cannot withdraw more money than
# his bank_balance and if the user enters any other input other than D, W or
# Q, the user will get an invalid selection message and the selection menu
# will be presented again.
while loop_active: 
    print(asterisks * width)
    print("PIXELL RIVER FINANCIAL".center(width))
    print("ATM Simulator\n".center(width))
    print(f"Your current balance is: ${bank_balance:,.2f}\n".center(width))
    print(f"Deposit: {menu_options[0]}".center(width))
    print(f"Withdraw: {menu_options[1]}".center(width))
    print(f"Quit: {menu_options[2]}".center(width))
    print(asterisks * width)
    user_selection = input("Enter your selection: ").upper()
    # This if statement checks to see if the user entered D (deposit) which is 
    # menu_options[0], it is the first element in the tuple menu_options.
    # If the user enters D, then the user is asked to enter the transaction
    # amount he wants to deposit. After the user has entered the amount
    # they wanted to deposit, then the user's bank balance is printed 
    # on the screen.
    # Then, after 3 seconds the screen is cleared.
    if user_selection == menu_options[0]:
        deposit = float(input("Enter the transaction amount: "))
        bank_balance += deposit
        print(f"\n{asterisks * width}")
        print(f"Your current balance is: ${bank_balance:,.2f}".center(width))
        print(asterisks * width)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    # This if statement checks to see if the user entered W (withdraw) which is
    # menu_options[1], it is the second element in the tuple menu_options.
    # If the user enters W, then the user is asked to enter the transaction
    # amount he wants to withdraw. After the user has entered the amount
    # they wanted to withdraw, then the user's bank balance is printed 
    # on the screen.
    # Note that the user can only withdraw equal to or less than the 
    # bank balance he has. This is checked in the if statement.
    elif user_selection == menu_options[1]:
        withdraw = float(input("Enter the transaction amount: "))
        # User's bank balance is checked to see if the bank balance is 
        # greater or equal to the amount he wants to withdraw, then if that's
        # true, bank balance is printed on the screen and the screen clears
        # after 3 seconds.
        if bank_balance >= withdraw:
            bank_balance -= withdraw
            print(f"\n{asterisks * width}")
            print(f"Your current balance is: ${bank_balance:,.2f}".center(width))
            print(asterisks * width)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        # If the withdraw amount enter was more than the bank balance
        # the user is presented with a message insufficient funds and the
        # screen is cleared after 3 seconds.
        else:
            print(f"\n{asterisks * width}")
            print("INSUFFICIENT FUNDS".center(width))
            print(asterisks * width)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
    # Now this elif statement checks if the user presses Q, that is the quit
    # menu/program option, which exits the program out of the while loop by 
    # changing the boolean value of loop_active to False.        
    elif user_selection == menu_options[2]:
        loop_active = False
    # After checking for all the options, we are left with the else statement
    # which prints invalid selection if the user enters any other values other
    # than D, W or Q. After that the screen is cleared after 3 seconds and 
    # the user is presented with the selection menu again.
    else:
        print(f"\n{asterisks * width}")
        print("INVALID SELECTION".center(width))
        print(asterisks * width)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')


        
            





    

    


