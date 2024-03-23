#!/usr/bin/python3
"""
Displays the state from the database.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def print_first_state(username, password, database_name):
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    username, password, database_name))


Session = sessionmaker(bind=engine)
session = Session()
first_state = session.query(State).order_by(State.id).first()
if first_state:
    print('{}: {}'.format(first_state.id, first_state.name))
else:
    print('Nothing')
    session.close()
    if __name__ == '__main__':
        if len(argv) == 4:
            print_first_state(argv[1], argv[2], argv[3])
            else:
                print(": {} <username> <password> <database>".format(argv[0]))
