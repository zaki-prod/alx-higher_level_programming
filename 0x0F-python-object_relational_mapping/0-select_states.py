#!/usr/bin/python3
#Lists all states drom the database hbtn_0e_0_usa.
#Usage: ./0-select_states.py <mysql username> \
#                            <mysql paasword> \
#                            <database name>
import sys 
import MySQLDB

if __name__ == "__main__":
    db = MySQLB.connect(user=sys.argv[1], paaswd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM  states")
    [print(state) for state in c.fetchall()]

