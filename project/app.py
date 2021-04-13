from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *
from model import *
from flask_login import LoginManager

from account.route import *
from book.route import *
from order.route import *





if __name__ == "__main__" :
    app.run()