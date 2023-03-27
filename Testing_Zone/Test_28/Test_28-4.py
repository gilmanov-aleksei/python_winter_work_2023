#! /usr/bin/python

from sqlalchemy import create_engine, MetaData, Table, Integer, String,Column
# from sqlalchemy import DateTime, ForeignKey, Numeric, SmallInteger
# from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost/sqlalchemy_tuts")

Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
Base.metadata.create_all(engine)