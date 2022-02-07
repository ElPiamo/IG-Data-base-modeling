import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name= Column(String(100), nullable=False)
    email= Column(String(150), unique=True, nullable=False)
    favorites= relationship("Favorites", back_populates="parent")

class Favorites(Base):
    __tablename__ = 'favorites'
    id= Column(Integer, primary_key=True)
    element_name= Column(String(20), nullable=False)
    total= Column(Integer, default=0)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")

class Elements(Base):
    __tablename__ = 'elements'
    id= Column(Integer, primary_key=True)
    url= Column(String(200), nullable=False)
    name= Column(String(200), nullable=False)
    favorites= Column(Integer, ForeignKey("favorites.id"))
    planets= relationship("Planets", back_populates="parent")
    vehicles= relationship("Vehicles", back_populates="parent")
    cheracters= relationship("Characters", back_populates="parent")

class Planets(Base):
    __tablename__= 'planets'
    id= Column(Integer, primary_key=True)
    population= Column(Integer, nullable=False)
    element_id= Column(Integer, ForeignKey("elements.id"))

class Vehicles(Base):
    __tablename__= 'vehicles'
    id= Column(Integer, primary_key=True)
    model= Column(String(100), nullable=False)
    manufacturer= Column(String(100), nullable=False)
    element_id= Column(Integer, ForeignKey("elements.id"))

class Characters(Base):
    __tablename__= 'characters'
    id= Column(Integer, primary_key=True)
    description= Column(String(200), nullable=False)
    gender= Column(String(20))
    element_id= Column(Integer, ForeignKey("elements.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')