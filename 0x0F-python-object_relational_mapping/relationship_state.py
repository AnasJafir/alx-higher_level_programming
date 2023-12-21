#!/usr/bin/python3
"""Start link class to table in database"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """State class
    Args:
        __tablename__ : name of MySQL table to store states
        id : states's id
        name : states's name
        cities : state-city relationship
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
