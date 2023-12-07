from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Test relationships and methods here
    company = session.query(Company).first()
    print("==============Company Freebies:===================")
    for freebie in company.get_freebies():
        print(f"Item: {freebie.item_name}, Value: {freebie.value}")

    print("\n==============Company Devs:=====================")
    for dev in company.get_devs():
        print(dev.name)

    dev = session.query(Dev).first()
    print("\n==============Dev Freebies:======================")
    for freebie in dev.get_freebies():
        print(f"Item: {freebie.item_name}, Value: {freebie.value}")

    print("\n==============Dev Companies:======================")
    for company in dev.get_companies():
        print(company.name)

    session.close()
