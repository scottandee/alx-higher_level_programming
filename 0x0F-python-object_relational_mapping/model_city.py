#!/usr/bin/python3
"""This script contains the City class declaration"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """This is the city class"""

    __tablename__ = "cities"
    id = Column("id", Integer(), primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer(), ForeignKey("states.id"),
                      nullable=False)
