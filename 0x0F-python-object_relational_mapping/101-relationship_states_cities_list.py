#!/usr/bin/python3
"""
Write a script that lists all State objects,
and corresponding City objects, contained in the
database hbtn_0e_101_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
The connection to your MySQL server must be to localhost
on port 3306
You must only use one query to the database
You must use the cities relationship for all State objects
Results must be sorted in ascending order by states.id and
cities.id
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

    # query database
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # commit the session
    session.commit()

    # close the sessioin
    session.close()
