from itertools import product

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from saleapp import db
from datetime import datetime
from saleapp import app
from flask_login import UserMixin
from enum import Enum as UserEnum

"""
lop BaseModel no ke thua lai db.model
vi id dung chung nhieu nen co the khai bao 1 lop rieng sau do cac lop khac ke thua lai
khoi mat cong de tao moi truong id
__abstract__ = True => giup no khong tao bang
"""
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

"""
Tao role de quan ly
"""
class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

"""
Tao bang user voi cac cot tuong ung
Bằng cách thừa kế từ UserMixin, bạn không cần phải định nghĩa lại các phương thức is_authenticated(), is_active(), is_anonymous(), get_id() 
"""
class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50))
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

"""
 category ke thua basemode tuc cung ke thua tu db.model=> no se hieu categoy se dai dien cho lop duoi CSDL
do Product nam duoi nen de trong dau ''
2 thuoc tinh quan trong la backref => khi khai bao thi no se tu dong them vao product
lazy = true => khi truy van lay danh muc no chi lay dung thong tin cua danh muc ko thuc hien lay products, khi tac dong moi lay
lazy = false/subquery => thi khi truy van vao category no lay luon product lam giam hieu nang
"""
class Category(BaseModel):
    __tablename__ = 'category' # tuong minh ten bang

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    # overwrite toString
    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False) # co 2 cach truyen vao cho foreignKey neu trong dau'' => dung ten bang 'cacategory.id'

    # overwrite toString
    def __str__(self):
        return self.name

# if __name__ == '__main__':
#     db.create_all()
# Sử dụng app.app_context() để tạo bảng
with app.app_context():
    # db.create_all()
    """
    them du lieu vao bang bang cac cau lenh nhu ben duoi
    """
    # c1 = Category(name='Dien thoai')
    # c2 = Category(name='May tinh bảng')
    # c3 = Category(name='Dong ho thong minh')
    #
    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)
    #
    # db.session.commit()
    """
    them du lieu vao bang tu tep json
    khi muon test voi session thi khong nen comment lai
    """
    products = [
                  {
                    "id": 1,
                    "name": "iphone 14",
                    "description": "Apple, 128GB, RAM: 6GB",
                    "price": 15000000,
                    "image": "images/pn1.jpg",
                    "category_id": 1
                  },
                  {
                    "id": 2,
                    "name": "iphone 15",
                    "description": "Apple, 128GB, RAM: 6GB",
                    "price": 20000000,
                    "image": "images/pn2.jpg",
                    "category_id": 1
                  },
                  {
                    "id": 3,
                    "name": "ipad Pro 11",
                    "description": "Apple, 128GB, RAM: 6GB",
                    "price": 14000000,
                    "image": "images/pn3.jpg",
                    "category_id": 2
                  }
                ]
    for p in products:
        prod = Product(name=p['name'],description=p['description'],price=p['price']
                       ,image=p['image'],category_id=p['category_id'])
        db.session.add(prod)
    # db.session.commit()