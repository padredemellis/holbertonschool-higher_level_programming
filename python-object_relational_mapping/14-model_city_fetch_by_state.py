#!/usr/bin/python3
"""Lista todas las ciudades con su estado usando ORM"""

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    results = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    session.close()