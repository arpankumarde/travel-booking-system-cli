# connect.py

def setCon():
    import mysql.connector as sql
    con = sql.connect(host='localhost', user='root',
                      passwd='your mysql passwowrd', database='travel_booking_system')
    if con.is_connected():
        cursor = con.cursor()
        return (con, cursor)
    else:
        exit()
