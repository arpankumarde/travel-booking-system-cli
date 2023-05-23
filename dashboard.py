# dashboard.py

import os
from rich import print
from time import gmtime, strftime


def start(con, cursor, uname, umail, uphone):
    os.system('cls')
    today = strftime("%a, %d %b %Y", gmtime())
    print("[bold cyan]Welcome to your Dashboard[/bold cyan]")
    print(f"Logged in as: {uname}")
    print(today)
    while True:
        try:
            menu = """\nEnter any of these:
    1. To book a new trip
    2. To view travel log
            """
            print(menu)
            c4 = int(input("\n>> "))
            if (c4 == 1):
                import booking
                booking.start(con, cursor, uname, umail, uphone)
            elif (c4 == 2):
                import history
                history.start(con, cursor, uname, umail, uphone)
            else:
                os.system('cls')
                print("That was an invalid input!")
        except:
            os.system('cls')
            print("That was an invalid input! Please try again")
