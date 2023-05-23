import os
from rich import print

from rich.console import Console
from rich.table import Table


def start(con, cursor, uname, umail, uphone):
    os.system('cls')
    q = f"SELECT uid FROM users WHERE umail='{umail}'"
    cursor.execute(q)
    uid = cursor.fetchone()[0]
    cursor.execute("SELECT pName FROM places")
    data = cursor.fetchall()
    place = []
    for row in data:
        place.append(row[0])
    q = f"SELECT bkDate,bkPickup,bkDrop,bkPersons,bkPrice FROM bookings WHERE uid={uid}"
    cursor.execute(q)
    act = cursor.fetchall()
    if (cursor.rowcount == 0):
        print("No travel activity found")
    else:
        table = Table(title="-- Your Travel Log --", style="",
                      show_edge=False, title_style="cyan bold")
        table.add_column("Booking Date", justify="center")
        table.add_column("PickUp")
        table.add_column("Drop")
        table.add_column("No. of travellers", justify="center")
        table.add_column("Amount", justify="right", min_width=10)
        for row in act:
            table.add_row(
                f"{row[0]}",
                f"{place[row[1]]}",
                f"{place[row[2]]}",
                f"{row[3]}",
                f"{row[4]}"
            )
        console = Console()
        console.print(table)
