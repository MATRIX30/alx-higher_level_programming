#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username, mysql
    password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running
    on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""

if __name__ == "__main__":
    # importing neccesary libraries
    import MySQLdb
    import sys

    # verify if right arguments have been supplied
    if len(sys.argv) < 4:
        print(
            "Usage:{:s} mysql username mysql password database name".format(
                sys.argv[0])
        )

    else:
        # setup database parameters
        db_username, db_password, db_name = sys.argv[1:]
        db_host = "localhost"
        db_port = 3306

        # establish database connection
        conn = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            passwd=db_password,
            db=db_name,
            charset="utf8",
        )

        # build and execute query
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
        records = cur.fetchall()

        # print out query result
        for record in records:
            print(record)

        # close all connections to db
        cur.close()
        conn.close()
