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
	session.commit()

add_product("")

def query_by_id(their_id):
   
  product = session.query(
       Product).filter_by(
       id=their_id).first()

  return product
query_by_id("")

def delete_product(their_id):
   
   session.query(Product).filter_by(
       id=their_id).delete()
   session.commit()
delete_product("")

