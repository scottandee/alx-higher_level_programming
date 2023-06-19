#!/usr/bin/python3
"""This script contains the State class declaration"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This is the states class"""

    __tablename__ = "states"

    id = Column("id", Integer(), primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
