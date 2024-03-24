#!/usr/bin/python3
"""List all State objects containing `a` from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def print_state():
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    rows = sess.query(State).all()
    for row in rows:
        if 'a' in row.__dict__['name']:
            print("{}: {}".format(row.__dict__['id'], row.__dict__['name']))
            sess.close()


if __name__ == "__main__":
    print_state()

