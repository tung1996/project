from flask import*
from flask import request
from order.controller import buy
from model import*

@app.route('/buy_book', methods= ['GET'])
def buy_book():
    return  buy.order()
    