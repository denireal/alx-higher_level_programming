#!/usr/bin/python3
"""
The script displays the State object with the name passed as an argument
from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def print_state_with_cities(username, password, database, state_name):
    """Prints the State object with associated cities."""
    # Create engine to connect to the database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query State and associated City objects
        result = (session.query(State.name, City.id, City.name)
                  .filter(State.id == City.state_id, State.name == state_name)
                  .all())

        # Print State and associated City information
        for state_name, city_id, city_name in result:
            print(f"{state_name}: ({city_id}) {city_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close session
        session.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function to print State object with associated cities
    print_state_with_cities(username, password, database, state_name)
