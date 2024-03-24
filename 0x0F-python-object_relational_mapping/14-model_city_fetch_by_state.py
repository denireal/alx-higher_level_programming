#!/usr/bin/python3
"""
The script displays the State object with the name passed as an argument
from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def display_city():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State, City).join(City).all()

    for ins in rows:
        print("{}: ({}) {}".format(ins[0].__dict__['name'],
                                   ins[1].__dict__['id'],
                                   ins[1].__dict__['name']))

    session.close()


if __name__ == "__main__":
    display_city()
