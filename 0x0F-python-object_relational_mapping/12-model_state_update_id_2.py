#!/usr/bin/python3
"""Update the name of the State object with the specified ID
in the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    # Create engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified ID and update its name
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'

    # Commit the transaction
    session.commit()

    # Close session
    session.close()
