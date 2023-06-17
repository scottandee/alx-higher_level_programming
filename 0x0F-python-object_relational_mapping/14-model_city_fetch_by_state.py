#!/usr/bin/python3
"""This script lists all cities that are in
a table and their respective states
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(State).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
