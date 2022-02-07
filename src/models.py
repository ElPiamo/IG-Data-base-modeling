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
    user_name = Column(String(100), nullable=False, unique=True)
    full_name= Column(String(150), nullable=False)
    password= Column(String(15), nullable=False)
    user_email = Column(String(50), nullable=False, unique=True)
    number_of_posts = Column(Integer, default=0)
    followers = Column(Integer, default = 0)
    following = Column(Integer, default=0)
    post= relationship("Post", back_populates="parent")

class Posts(Base):
    __tablename__ = 'posts'
    id= Column(Integer, primary_key=True)
    caption= Column(String(1000), nullable=True)
    comments= Column(String(1000), nullable = True)
    likes = Column(Integer, default =0)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")
    pictures= relationship("Pictures", back_populates="parent")
    reels= relationship("Reels", back_populates="parent")
    ig_tv= relationship("IGTV", back_populates="parent")

class Pictures(Base):
    __tablename__ = 'pictures'
    id= Column(Integer, primary_key=True)
    tags= Column(Integer, nullable=False)
    location = Column(String(200), nullable=True, unique=False)
    posts_id= Column(Integer, ForeignKey("posts.id"))
    
class Reels(Base):
    __tablename__= 'reels'
    id= Column(Integer, primary_key=True)
    views= Column(Integer, default=0)
    audio = Column(String(200), nullable=True)
    element_id= Column(Integer, ForeignKey("posts.id"))

class IGTV(Base):
    __tablename__= 'igtv'
    id= Column(Integer, primary_key=True)
    views= Column(Integer, default=0)
    element_id= Column(Integer, ForeignKey("posts.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')