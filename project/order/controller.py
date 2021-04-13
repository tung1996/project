from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask_admin import Admin
from flask_login import current_user, login_user
from config import *
from model import *

class buy() :
    def order(self) :
        if current_user.is_authenticated :
            if current_user.admin == 1 :
                return "You are the admin so you cannot buy"
            else :
                name_book = request.args.get("name_book")
                name_quantity = {"hai so phan":2 , 'nha gia kim' : 1 }

                order = Order(current_user.id)
                db.session.add(order)
                db.session.commit()
                total_money = 0
                for name,quantity in name_quantity.items() :
                    book = Book.query.filter_by(name =name ).first()
                    price = book.price
                    details = Order_details(order , book.id , quantity , price )
                    db.session.add(details)
                    db.session.commit()
                    # new_quantity = float(quantity)
                    total_money +=  price*quantity

                update = Order.query.filter_by(id = details.order_id ).first()
                new = Order.query.get(update.id)
                new.total_money = total_money 
                db.session.commit()

                return "you have placed your order successfully"
        else :
            return "You need to sign in to your account"

buy = buy ()