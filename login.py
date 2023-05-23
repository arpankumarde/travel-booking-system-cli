# login.py
import os
from time import sleep

import maskpass
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
    print("[bold cyan]Login to your Bengal Traveller Account[/bold cyan]\n")
    while (True):
        pass1, email = '', ''
        while (True):
            email = input('Please enter your email: ')
            email = email.lower()
            if (validateEmail(email) == 'OK'):
                break
            else:
                print('The email is invalid!')
        pass1 = maskpass.askpass(
            prompt="Please enter your password: ", mask="*")
        if (len(pass1) >= 8 and len(pass1) <= 20):
            try:
                q = "SELECT * FROM users WHERE umail='"+email+"' AND upass='"+pass1+"';"
                cursor.execute(q)
                data = cursor.fetchall()[0]
                uname = data[1]
                uphone = data[2]
                umail = data[3]
                break
            except:
                print('[red bold]Login Unsuccessful[/red bold]: ', end='')
                print('Invalid Credentials! Please try again\n')
        else:
            print('[red bold]Login Unsuccessful[/red bold]: ', end='')
            print('Invalid Credentials! Please try again\n')
    if (len(uname) != 0 and len(umail) != 0):
        print('\n[green bold]Login Successful![/green bold]')
        print('[bold cyan]Redirecting to Dashboard...[/bold cyan]')
        sleep(1.5)
        import dashboard
        dashboard.start(con, cursor, uname, umail, uphone)
