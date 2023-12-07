#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create sample data
    company1 = Company(name='Safaricom', founding_year=2000)
    company2 = Company(name='Google', founding_year=1995)

    dev1 = Dev(name='Mark Mwangi')
    dev2 = Dev(name='Steve Maina')

    freebie1 = Freebie(item_name='Macbook Pro', value=10, dev=dev1, company=company1)
    freebie2 = Freebie(item_name='Logitech MX', value=20, dev=dev2, company=company2)

    session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
    session.commit()

    session.close()
