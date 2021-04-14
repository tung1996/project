from flask import*
from flask import request
from order.controller import buy
from model import*
from order.all_order_controller import *

@app.route('/buy_book', methods= ['GET'])
def buy_book():
    return  buy.order()

# thong ke don hang
app.register_blueprint(check, url_prefix = "/admin" )

    