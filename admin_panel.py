# admin_panel.py

import datetime
import os
from time import sleep
from rich import print
from rich.console import Console
from rich.table import Table


def start(con, cursor, adname, admail):
    os.system('cls')
    print("[bold cyan]Bengal Travels Admin Panel[/bold cyan]")
    print(f"Logged in as: {adname}")
    while (True):
        try:
            menu = """
Enter any of the following to continue:
    1. Manage Admins
    2. See Booking Stats
Press [bold red]0[/bold red] to Go back to the main menu
            """
            print(menu)
            print(">>> ", end='')
            n = int(input())
            os.system('cls')
            if (n == 0):
                print("Loading Main menu...")
                sleep(1.3)
                os.system('cls')
                break
            elif (n == 1):
                q = "SELECT adid, adname, admail FROM admins"
                cursor.execute(q)
                data = cursor.fetchall()
                table = Table(title="--Bengal Travel Admins--",
                              header_style="bold red")
                table.add_column("Admin ID")
                table.add_column("Admin Name")
                table.add_column("Admin Email")
                for row in data:
                    table.add_row(
                        f"{row[0]}",
                        f"{row[1]}",
                        f"{row[2]}"
                    )

                console = Console()
                console.print(table)
                menu = """
    1. Add Admin
    2. Remove Admin
                """
                print(menu)
                print(">>> ", end='')
                n = int(input())
            elif (n == 2):
                print("[bold cyan]Booking Status:\n[/bold cyan]")
                today = datetime.date.today()
                startdate = today - datetime.timedelta(days=7)
                cursor.execute(
                    f"SELECT count(*) from bookings where bkdate>='{startdate}'")
                data = cursor.fetchall()[0][0]
                print(f"Bookings in the Last 7 days: {data}")
                startdate = today - datetime.timedelta(days=30)
                cursor.execute(
                    f"SELECT count(*) from bookings where bkdate>='{startdate}'")
                data = cursor.fetchall()[0][0]
                print(f"Bookings in the Last 30 days: {data}")
            else:
                os.system('cls')
                print("That was an invalid input! Please try again")
        except:
            os.system('cls')
            print("That was an invalid input! Please try again")
