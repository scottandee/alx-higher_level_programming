#!/usr/bin/python3
"""This script finds the id of states passed as argument"""


from model_state import Base, State
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
    state = session.query(State).filter(State.name == [sys.argv[4]]).first()
    if (state is None):
        print("Not found")
    else:
        print(state.id)
    session.close()
