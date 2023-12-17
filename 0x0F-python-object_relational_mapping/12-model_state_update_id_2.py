#!/usr/bin/python3
"""
Write a script that changes the name of a State object
from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from
model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
Change the name of the State where id = 2 to New Mexico
Your code should not be executed when imported
"""
if __name__ == "__main__":
    # import necessary libraries
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    # create engine to support db connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query for object to modify by id
    res = session.query(State).filter(State.id == 7).first()

    # modify object's name attribute
    res.name = "Bamenda"

    # commit changes to session
    session.commit()

    # close the session
    session.close()
