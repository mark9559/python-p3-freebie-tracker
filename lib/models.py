from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship('Freebie', backref='company')

    def __repr__(self):
        return f'<Company {self.name}>'

    def get_freebies(self):
        return self.freebies

    def get_devs(self):
        return list({freebie.dev for freebie in self.freebies})

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'

    def get_freebies(self):
        return self.freebies

    def get_companies(self):
        return list({freebie.company for freebie in self.freebies})

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    def __repr__(self):
        return f'<Freebie {self.item_name}>'
