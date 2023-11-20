#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MYSQLdb


if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=argv[1],
                         passwrd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
