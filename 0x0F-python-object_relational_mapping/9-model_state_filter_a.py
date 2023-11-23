#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

     # Query and print State objects containing the letter 'a'
    statess = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
        .all()
    )

    for state in statess:
        print("{}: {}".format(state.id, state.name))
    session.close()