#!/usr/bin/python3
'''to list objects'''

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
session.close()
