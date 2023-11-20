#!/usr/bin/python3
"""akes in the name of a state as an argument
and lists all cities of that state"""
from sys import argv
import MYSQLdb


if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=argv[1],
                         passwrd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM
                 cities JOIN states ON cities.id=states.id
                 WHERE states.name = '{}';""".format(argv[4]))
    states = curs.fetchall()
    
    print(", ".join([state[1] for state in states]))
