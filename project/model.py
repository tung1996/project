from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from config import *


class Book(db.Model):
    __tablename__= "book"
    id = Column( Integer , primary_key = True , autoincrement = True , nullable = False )
    name = Column( String(255) , nullable = False)
    price = Column( Float() , nullable = False)
    def __init__(self , name, price ):
        self.name = name
        self.price = price

   

class Account(db.Model,UserMixin):
    __tablename__= "account"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False )
    username = Column( String(30) , nullable = False)
    password = Column( String(255), nullable = False) 
    fullname = Column ( String(50) , nullable = False)
    admin = Column( Integer , autoincrement = True) # neu la ad thi note là "1" con khong phai note vào "0"
    def __init__(self , username , password ,fullname , admin ) :
        self.username = username
        self.password = password
        self.fullname = fullname
        self.admin = admin

class Order(db.Model):
    __tablename__= "order"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    account_id = Column( Integer , ForeignKey(Account.id) , nullable = False )
    total_money = Column ( Float() , default = 0 , nullable = False)
    Order_details = relationship("Order_details" , backref = "order" , lazy= False)
    def __init__(self , account_id , total_money ):
        self.account_id = account_id
        self.total_money = total_money

class Order_details (db.Model):
    __tablename__= "order_details"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    order_id = Column( Integer , ForeignKey(Order.id) , nullable = False )
    book_id = Column( Integer , ForeignKey(Book.id) , nullable = False )
    quantity = Column(Integer ,default = 0 )
    into_money = Column (Float() ,default = 0 )
    def __init__(self ,order , book_id, quantity ,into_money ):
        self.order  = order
        self.book_id = book_id
        self.quantity = quantity
        self.into_money = into_money 

@login.user_loader
def load_user(id):
    return Account.query.get(int(id))


db.create_all()