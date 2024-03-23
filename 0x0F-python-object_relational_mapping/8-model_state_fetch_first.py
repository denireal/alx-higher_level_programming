#!/usr/bin/python3
"""
Displays the state from the database.
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session


def print_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}?autocommit=true".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()

if first_state:
    print("{}: {}".format(first_state.id, first_state.name))
else:
    print("Nothing")
    session.close()


if __name__ == "__main__":
    print_state()
