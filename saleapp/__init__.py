from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
"""
    xac dinh bien app se dung nhieu cho khac nhau nen dat ben trong init(file khoi dong package)
    name: bien toan cuc truyen vao
"""
app = Flask(__name__)
"""
giup cap nhat vao sql khong bi loi ta them secret_key
"""
app.secret_key = '&6213$#%&%$#$&)(sfsdfsf#*-+*/'
"""
cau hinh thong so ket noi
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/labsaledb?charset=utf8mb4'
"""
cai dat PAGE_SIZE de sau dung chung
"""
app.config['PAGE_SIZE'] = 4
"""
cai dat PAGE_COMMENT_SIZE de sau dung chung
"""
app.config['PAGE_COMMENT_SIZE'] = 6
"""
Can cau hinh ket noi
"""
db = SQLAlchemy(app=app)
""""""
cloudinary.config(
    cloud_name= 'djdcw29s3',
    api_key= '911457233263351',
    api_secret= 'ynjQIgN2-hHGsH3jeEITP7Q6I1M'
)
"""
tao bie login truyen app vao de no biet quan ly app nao cua minh
"""
login = LoginManager(app=app)