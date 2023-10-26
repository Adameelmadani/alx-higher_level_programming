#!/usr/bin/python3
"""
This is our module
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import urllib.parse


if __name__ == "__main__":
    q_passw = urllib.parse.quote_plus(sys.argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], q_passw, sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id.asc()).all()
    for result in results:
        print("{}: {}".format(result.id, result.name))
