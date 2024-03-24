#!/usr/bin/python3
"""List all State objects containing argument from db

This script connects to a MySQL database and retrieves all
State objects from the table. It then checks each State object's
name attribute to see if it contains the specified argument provided
as a command-line argument. If any State object's name contains the
specified argument, it prints the ID of that State object. If no
matching State objects are found in the database, it prints "Not Found".

Usage:
    ./script.py <username> <password> <database> <argument>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_arg_state_obj():
    # Create engine to connect to the database

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the specified argument
    states_with_arg = session.query(State).filter(
            State.name.like('%{}%'.format(sys.argv[4]))).all()

    # If any matching State objects found, print their IDs
    if states_with_arg:
        for state in states_with_arg:
            print(state.id)
    else:
        print("Not Found")

    # Close session
    session.close()


if __name__ == "__main__":
    list_arg_state_obj()
