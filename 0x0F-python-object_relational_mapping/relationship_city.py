#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class
    Args:
        __tablename__ : name of MySQL table to store cities
        id : city's id
        name : city's name
        state_id : city's state id (foreign key linked to states.id)
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
