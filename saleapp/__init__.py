from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
    xac dinh bien app se dung nhieu cho khac nhau nen dat ben trong init(file khoi dong package)
    name: bien toan cuc truyen vao
"""
app = Flask(__name__)
"""
cau hinh thong so ket noi
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/labsaledb?charset=utf8mb4'

"""
Can cau hinh ket noi
"""
db = SQLAlchemy(app=app)