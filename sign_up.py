# sign_up.py
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
    print("[bold cyan]Sign up with Bengal Travels[/bold cyan]\n")
    name, email = '', ''
    while (True):
        name = input('Please enter your name: ')
        if not name:
            print('Name cannot be empty!')
        else:
            break
    while (True):
        email = input('Please enter your email: ')
        email = email.lower()
        q = "SELECT count(*) as count FROM users WHERE umail='"+email+"'"
        cursor.execute(q)
        if (cursor.fetchone()[0] != 0):
            print(
                '[red bold]This email is already in use with another account! Try logging in instead![/red bold]\n')
        else:
            if (validateEmail(email) == 'OK'):
                break
            else:
                print('[red bold]The email is invalid![/red bold]\n')
    while (True):
        phone = int(input('Please enter your phone number: '))
        if not phone:
            print('Please enter a valid phone number')
        else:
            break
    while (True):
        pass1 = maskpass.askpass(
            prompt="Please enter your password[8 to 20 characters]: ", mask="*")
        if (len(pass1) >= 8 and len(pass1) <= 20):
            pass2 = maskpass.askpass(
                prompt="Please re-enter your password: ", mask="*")
            if (pass1 == pass2):
                break
            else:
                print('[bold red]The passwords do not match[/bold red]\n')
        else:
            print(
                '[bold red]The password must contain 8 charaters upto 20 characters(at max)![/bold red]\n')
    q = f"INSERT INTO users(uName,uPhone,uMail,uPass) values('{name}',{phone},'{email}','{pass1}')"
    cursor.execute(q)
    con.commit()
    print('\n[green bold]Account Created Successfully![/green bold]')
    print('[bold cyan]Redirecting to User Dashboard...[/bold cyan]')
    sleep(1.3)
    import dashboard
    dashboard.start(con, cursor, name, email, phone)
