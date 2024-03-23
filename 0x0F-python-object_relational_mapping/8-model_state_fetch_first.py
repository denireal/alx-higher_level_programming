#!/usr/bin/python3
"""
Displays the state from the database.
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session


def print_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    for rows_ in rows:
        print("{}: {}".format(rows_.__dict__['id'], rows_.__dict__['name']))


    session.close()

if __name__ == "__main__":
    print_state()
