#!/usr/bin/python3
"""
Script has class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that represents a city.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The ID of the state to which the city belongs.
    """
    __tablename__ = 'cities'
    i = Column(Integer, unique=True, nullable=False, primary_key=True)
    n = Column(String(128), nullable=False)
    s_id = Column(Integer, ForeignKey("states.id"), nullable=False)
