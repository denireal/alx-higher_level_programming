#!/usr/bin/python3
"""Deletes State objects from the database whose names contain the
letter 'a'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_letter_a(username, password, database):
    """Deletes State objects from the database whose names contain letter 'a'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    # Create engine to connect to the database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects whose names contain the letter 'a'
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)

    # Commit the transaction
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to delete State objects with letter 'a'
    delete_states_with_letter_a(username, password, database)
