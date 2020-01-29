from model import *
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_meme(title, description, img_url):
	object_meme = Meme(
		title = title,
		description = description,
		image_url = img_url)
	session.add(object_meme)
	session.commit()

def get_id(title, description, img_url):
	meme_object = session.query(Meme).filter_by( title=title, description=description, img_url=img_url).first()
	return meme_object.id


def get_all_memes():
	memes = session.query(Meme).all()
	return memes

def change_info( title, description, img_url):
	declarative_base = session.query(Meme).filter_by(title=title).first()
	declarative_base.description = description
	declarative_base.image_url = img_url	
	session.commit()
#create_meme("title", "description", "img.png")
# create_meme("Abdalla", "Abdalla isn't so scary", "../static/img/Abdalla.jpeg")