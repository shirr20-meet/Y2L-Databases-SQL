from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):
	product_object = Product (
	name = name,
	price = price,
	picture_link = picture_link,
	description = description )
	session.add(product_object)
	session.commit()

add_product("")

def update_lab_status(id, name):
  
   student_object = session.query(
       Student).filter_by(
       name=name).first()
   student_object.name = name
   session.commit()


def delete_product(their_id):
   
   session.query(Product).filter_by(
       id=their_id).delete()
   session.commit()
delete_product("")

def query_all():
	students = session.query(
      Student).all()
  	return students


def query_by_id(their_id):
	student = session.query(
       Student).filter_by(
       id=their_id).first()
   	return student

def Add_To_Cart(productID):
	Cart_object = Cart (
		productID = productID)
	session.add(product_object)
	session.commit()