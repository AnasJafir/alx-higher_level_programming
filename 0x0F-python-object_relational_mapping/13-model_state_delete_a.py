#!/usr/bin/python3
"""List all states from a database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    del_state = session.query(State).filter(State.name.like('%a%'))
    for state in del_state:
        session.delete(state)
    session.commit()
    session.close()
