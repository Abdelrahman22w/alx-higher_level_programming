#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


mymetadata = metadata()
Base = declarative_base(metadata = mymetadata)

class State(Base):
    """
    Class defines each state
    """
    __tablename__ = 'States'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
