#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print(
            "Usage: {} username password database_name state_name".format(
                argv[0]
            )
            )
        exit(1)
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    statess = session.query(State).filter(State.name == argv[4]).first()

    if statess:
        print("{}".format(statess.id))
    else:
        print("Not found")
    session.close()
