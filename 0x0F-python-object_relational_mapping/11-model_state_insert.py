#!/usr/bin/python3
"""Prints the ID of the State object with the specified name from the database.

This script connects to a MySQL server running on localhost at port 3306 and
prints the ID of the State object with the specified name. It takes three
arguments:
    1. MySQL username
    2. MySQL password
    3. Database name

Usage:
    ./script.py <username> <password> <database>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create engine to connect to the database
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)

    # Create session
    Session = sessionmaker(bind=eng)
    sess = Session()

    # Add a new State object to the database
    state = State(name='Louisiana')
    sess.add(state)
    
    # Query the newly added State object by name and print its ID
    state_query = sess.query(State).filter_by(name='Louisiana').first()
    print(state_query.id)

    # Commit the transaction
    sess.commit()

    # Close session
    sess.close()
