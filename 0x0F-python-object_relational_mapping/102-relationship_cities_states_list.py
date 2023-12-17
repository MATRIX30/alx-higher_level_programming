#!/usr/bin/python3
"""
Write a script that lists all City objects from
the database hbtn_0e_101_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running
on localhost at port 3306
You must use only one query to the database
You must use the state relationship to access to the
State object linked to the City object
Results must be sorted in ascending order by cities.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
    # import necessary libraries
    import sys
    from relationship_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City

    # create an engine to manage connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database and display
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # commit the session
    session.commit()

    # close the sessioin
    session.close()
