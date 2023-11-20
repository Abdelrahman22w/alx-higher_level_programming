#!/usr/bin/python3
"""script that takes in an argument
 and displays all values in the states table of hbtn_0e_0_usa"""
from sys import argv
import MYSQLdb


if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=argv[1],
                         passwrd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                 .format(argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
