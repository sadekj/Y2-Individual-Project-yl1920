from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Meme(Base):
	__tablename__ = "meme"
	id = Column(Integer, primary_key=True)
	title = Column(String)
	description = Column(String)
	image_url = Column(String)  # default="/static/img/images.png"
  