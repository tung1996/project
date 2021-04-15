from flask import Flask,request,Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_login import current_user,login_user
from model import *

check = Blueprint("check" , __name__)
@check.route("/all_order") 
def all_user():
    if current_user.is_authenticated :
        if current_user.admin == 1 :
            order_id = []
            order_details = []
            all_order = []
            quantity = []
            detail = []
            name_account = request.args.get("name_account")
            if name_account != None :
                user = Account.query.filter_by(username = name_account ).first()
                try : 
                    orders = Order.query.filter_by(account_id = user.id ).all()
                    for order in orders :
                        order_id.append(order.id)
                    for x in order_id :
                        details = Order_details.query.filter_by(order_id = x).all()
                        for detail in details :
                            order_details.append(detail.book_id)
                            quantity.append(detail.quantity)
                    for z in order_details :
                        book = Book.query.get(z)
                        all_order.append(book.name)
                    total = db.session.query(db.func.sum(Order.total_money)).filter(Order.account_id == user.id ).scalar()
                    return ({"all order user": all_order , "quantity" : quantity , "total_money" : total })
                except : 
                    return "user does not make a purchase or wrong user"
            else :
                data = Order_details.query.distinct(Order_details.book_id)
                for book in data :
                    books = Book.query.get(book.book_id)
                    all_order.append(books.name)
                    quantity.append(book.quantity)
                total = db.session.query(db.func.sum(Order.total_money)).scalar()
                return ({"all order" : all_order ,"quantity" : quantity  ,"total" : total})
        else :
            return "You are not an administrator"
    else :
        return "You need to log in"
   
    