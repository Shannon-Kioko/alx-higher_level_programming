#!/usr/bin/python3
"""
Script that prints the first State object from the database
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

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    statess = session.query(State).order_by(State.id).first()

    if statess:
        print("{}: {}".format(statess.id, statess.name))
    else:
        print("Nothing")
    session.close()
