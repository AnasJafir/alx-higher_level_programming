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
    new_state = session.query(State).filter_by(id=2).first()
    if new_state:
        new_state.name = 'New Mexico'
        session.commit()
    session.close()
