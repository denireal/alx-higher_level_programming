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


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
