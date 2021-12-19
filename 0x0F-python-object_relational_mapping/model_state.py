#!/usr/bin/python3
''' declarative_base() callable returns a new base class'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''classs definitipon'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
