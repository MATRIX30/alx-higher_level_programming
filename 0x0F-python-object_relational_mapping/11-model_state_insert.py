#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    # create an engine to manage connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True)

    # create new State
    new_state = State(name="Louisiana")

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # add state object to  session
    session.add(new_state)

    # commit session
    session.commit()

    # query to get id of new state Created
    res = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(res.id))
    # close session
    session.close()
