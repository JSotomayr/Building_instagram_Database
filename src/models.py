import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('follower', Base.metadata,
    Column('user_from_id', ForeignKey('user.id')),
    Column('user_to_id', ForeignKey('user.id'))
)

association_table = Table('like', Base.metadata,
    Column('post_id', ForeignKey('post.id')),
    Column('user_id', ForeignKey('user.id'))
)
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique= True, nullable=False)
    password = Column(String, nullable=False)
    profilephoto = Column(nullable=True)
    nickname = Column(String, nullable=False)
    description = Column(String, nullable=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String, nullable=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, unique=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    mediaurl = Column(String, nullable=False)
    type = Enum('Photo', 'Video')

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e