#!/usr/bin/python3
"""
Write a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)

Your script should take 3 arguments: mysql username, mysql
password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on
localhost at port 3306
You must use the cities relationship for all State objects
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
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create the state California with city
    # San Francisco
    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)

    # add new_state
    session.add_all([new_state, new_city])

    # commit the session
    session.commit()

    # close the sessioin
    session.close()
