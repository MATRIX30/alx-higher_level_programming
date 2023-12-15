#!/usr/bin/python3

"""
Once again, write a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database
name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost
at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
if __name__ == "__main__":
    # importing neccesary libraries
    import MySQLdb
    import sys

    # verify if right arguments have been supplied
    if len(sys.argv) < 5:
        print(
            "Usage:{:s} mysql username mysql password database name".format(
                sys.argv[0])
        )

    else:
        # setup database parameters
        db_username, db_password, db_name, user_input = sys.argv[1:]
        db_host = "localhost"
        db_port = 3306

        # clean input against sql injection
        user_input = user_input.replace(":", "")
        user_input = user_input.replace("'", "")

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
        cur.execute(
            "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(
                user_input
            )
            )
        records = cur.fetchall()

        # print out query result
        [print(record) for record in records if record[1] == user_input]

        # close all connections to db
        cur.close()
        conn.close()
