#!/usr/bin/python3
"""
Displays State object with the name passed as argument from the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).order_by(State.id):
        print(i.id, i.name, sep=": ")
        for query_city in i.cities:
            print("    ", end="")
            print(query_city.id, query_city.name, sep=": ")
