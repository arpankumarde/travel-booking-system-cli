# admin.py

import os
import maskpass
from time import sleep
from rich import print


def validateEmail(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return ('OK')
    else:
        return ('ERROR')


def start(con, cursor):
    os.system('cls')
    print("[bold cyan]Bengal Travel Admin Login[/bold cyan]\n")
    while (True):
        pass1, email = '', ''
        while (True):
            email = input('Please enter your email: ')
            email = email.lower()
            if (validateEmail(email) == 'OK'):
                break
            else:
                print('[red bold]Invalid Email[/red bold]\n')
        pass1 = maskpass.askpass(
            prompt="Please enter your password: ", mask="*")
        try:
            q = "SELECT * FROM admins WHERE admail='"+email+"' AND adpass='"+pass1+"';"
            cursor.execute(q)
            data = cursor.fetchall()[0]
            adname = data[1]
            admail = data[2]
            break
        except:
            print('\n[red bold]Login Unsuccessful[/red bold]: ', end='')
            print('Invalid Credentials! Please try again\n')
    if (len(adname) != 0 and len(admail) != 0):
        print('\n[green bold]Login Successful:[/green bold] ', end='')
        print('Redirecting to Admin Panel...')
        sleep(1.3)
        import admin_panel
        admin_panel.start(con, cursor, adname, admail)
