#!/usr/bin/python3
"""Lista estados que contienen la letra 'a'"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    session.close()