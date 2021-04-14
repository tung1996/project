from flask import*
from flask import request
# import requests
from book.controller import filter_all 
from model import* 

# tim kiem sach
@app.route('/book', methods= ['GET'])
def book():
    return filter_all.filter()