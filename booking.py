# booking.py

import os
from rich import print
from datetime import *


def start(con, cursor, uname, umail, uphone):
    q = f"SELECT uid FROM users WHERE uMail='{umail}'"
    cursor.execute(q)
    uid = cursor.fetchone()[0]
    os.system('cls')
    print("[bold cyan]Welcome to the Booking Portal[/bold cyan]")
    print(f"Logged in as: {uname}")
    print("\n[red bold]NOTE: [/red bold]We only rent our cars from Kolkata to popular destinations and vice versa only")
    while True:
        cursor.execute('SELECT * FROM Places')
        data = cursor.fetchall()
        places = []
        for row in data:
            places.append(row[1].capitalize())
        while True:
            pickup = input("\nEnter the Pickup Location: ").capitalize()
            drop = input("Enter the Drop Location: ").capitalize()
            if (pickup == drop):
                print(
                    "[red bold]Error: [/red bold] Pickup and Drop Location cannot be same!")
            elif (pickup == 'Kolkata'):
                if (drop in places):
                    q = f"SELECT * FROM places WHERE pName = '{drop}'"
                    break
                else:
                    print(
                        f"Sorry! We don't serve {drop} at the moment. Please try a different location.")
            elif (drop == 'Kolkata'):
                if (pickup in places):
                    q = f"SELECT * FROM places WHERE pName = '{pickup}'"
                    break
                else:
                    print(
                        f"Sorry! We don't serve {pickup} at the moment. Please try a different location.")
            else:
                print(
                    '[yellow bold]Warning: [/yellow bold]One among the Pickup or the Drop location has to be Kolkata')
        cursor.execute(q)
        dist = cursor.fetchone()[2]
        q = f"SELECT pID FROM places WHERE pName='{pickup}'"
        cursor.execute(q)
        pickupcode = cursor.fetchone()[0]
        q = f"SELECT pID FROM places WHERE pName='{drop}'"
        cursor.execute(q)
        dropcode = cursor.fetchone()[0]
        while True:
            today = date.today()
            tdate = input("\nEnter the Pickup Date[YYYY-MM-DD]: ")
            bkdate = date(int(tdate[:4]), int(tdate[5:7]), int(tdate[8:]))
            if (bkdate > today):
                break
            else:
                print(
                    "[red bold]Error: [/red bold]Booking Date cannot be today or any previous days!")
        while True:
            bktime = input("\nEnter the Pickup Time[HH.MM]: ")
            if (len(bktime) <= 1):
                bktime = '0'+bktime
            if ('.' not in bktime.split()):
                bktime = bktime[:2]+'.00'
            bktime = bktime[:5]
            if (int(bktime[:2]) < 24 and int(bktime[3:]) < 60):
                break
            else:
                print("[red bold]Error: [/red bold]Invalid Time Entered!")
        while True:
            pcount = int(
                input("\nHow many people will be travelling by the car altogether? "))
            if (pcount > 0 and pcount <= 8):
                break
            else:
                print(
                    "[red bold]Error: [/red bold]Invalid Input! Maximum of 8 people can travel together")
        if (pcount <= 2):
            xcode = 'S'
        elif (pcount <= 4):
            xcode = 'M'
        else:
            xcode = 'L'
        q = f"select cprice from cars where cid='{xcode}'"
        cursor.execute(q)
        xcost = cursor.fetchone()[0]
        cost = xcost*dist
        os.system('cls')
        print("[cyan bold]Booking Details[/cyan bold]\n")
        print(
            f"[bold]Pickup Location:[/bold] [yellow bold]{pickup}[/yellow bold]")
        print(f"[bold]Drop Location:[/bold] [yellow bold]{drop}[/yellow bold]")
        print(f"[bold]Pickup date:[/bold] [yellow bold]{bkdate}[/yellow bold]")
        print(
            f"[bold]Pickup time:[/bold] [yellow bold]{bktime} Hrs[/yellow bold]\n")
        print(f"[bold]Booked by:[/bold] [yellow bold]{uname}[/yellow bold]")
        print(f"[bold]Email ID:[/bold] [yellow bold]{umail}[/yellow bold]")
        print(
            f"[bold]Contact number:[/bold] [yellow bold]{uphone}[/yellow bold]\n")

        print(
            f"[bold]Total no. of Travellers:[/bold] [yellow bold]{pcount}[/yellow bold]")
        print(
            f"[bold]Total Distance:[/bold] [yellow bold]{dist} km[/yellow bold]")
        print(
            f"[bold]Total Amount Payable:[/bold] [yellow bold]Rs.{cost}[/yellow bold]\n")
        print("[bold][red]NOTE:[/red] Toll taxes are not included.\nThey have to be paid by the traveller during the journey[/bold]\n")
        print(
            "Enter [bold]Y[/bold] to confirm the booking, Press [bold]N[/bold] to cancel")
        cnf = input(">> ").capitalize()[0]
        if (cnf == 'Y'):
            q = f"INSERT INTO Bookings(uid,bkPickup,bkDrop,bkDate,bkTime,bkPersons,cID,bkDist,bkPrice) VALUES({uid},{pickupcode},{dropcode},'{bkdate}',{float(bktime)},{pcount},'{xcode}',{dist},{cost})"
            cursor.execute(q)
            con.commit()
            print("\n[green bold]Hurray![/green bold] Booking confirmed!")
            break
        else:
            print("[red bold]Booking cancelled![/red bold]")
            break
