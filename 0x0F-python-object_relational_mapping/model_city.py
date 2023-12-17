#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an
auto-generated, unique integer, can’t be null and is
a primary key
class attribute name that represents a column of a string
of 128 characters and can’t be null
class attribute state_id that represents a column of an integer,
can’t be null and is a foreign key to states.id
You must use the module SQLAlchemy
"""

from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from model_state import Base, State


class City(Base):
    """implementation for city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", backref=backref("cities", order_by=id))

# create tables
# Base.metadata.create_all(engine)
