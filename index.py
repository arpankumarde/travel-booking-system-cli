# Travel-Booking-System
# index.py


import os
from time import sleep
from rich import print

import connect
con, cursor = connect.setCon()

os.system('cls')
print('[bold cyan]Welcome to Bengal Travels[/bold cyan]')
while (True):
    try:
        menu = """
Press any of the following to continue:
    1. Create new account
    2. User login
    3. Admin login
Type [bold red]0[/bold red] to exit our menu
        """
        print(menu)
        print(">>> ", end='')
        n = int(input())
        if (n == 0):
            print("Thank you for visiting us")
            print("[red bold]Exiting CLI...[/red bold]")
            sleep(0.3)
            break
        elif (n == 1):
            import sign_up
            sign_up.start(con, cursor)
        elif (n == 2):
            import login
            login.start(con, cursor)
        elif (n == 3):
            import admin
            admin.start(con, cursor)
        else:
            os.system('cls')
            print("That was an invalid input! Please try again")
    except:
        os.system('cls')
        print("That was an invalid input! Please try again")
