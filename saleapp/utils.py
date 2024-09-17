import json, os

from saleapp import app, db
from saleapp.models import Category, Product, User
import hashlib # giup bam password

"""
Ham doc file json
than ham co 2 cach viet co the dung f.close hoac dung with
    # f = open(path,"r")
    # data = json.load(f)
    # f.close()
    # return data
"""
def read_json(path):
    with open(path,"r") as f:
        return json.load(f)


"""
Doc categories
Doc products
  doc tuong doi : data/categories.json
  doc tuyet doi : nen dung bang cach import them os va app => da comment
  dung models de lay du lieu bang query
"""
def load_categories():
    category = Category.query.all()
    return category
    # return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products(cate_id=None, keyword=None, from_price=None, to_price=None, page = 1):
    '''Cac mat hang kinh doanh phai la active true'''
    products = Product.query.filter(Product.active.__eq__(True))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if keyword:
        products = products.filter(Product.name.contains(keyword))

    if from_price:
        products = products.filter(Product.price.__ge__(from_price))

    if to_price:
        products = products.filter(Product.price.__le__(to_price))

    """
    lay gia tri page_size dacai dat khi khoi tao
    select * from product limit page_size offset 0
    """
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size

    return products.slice(start, end).all() # them .all de neu khong co la no se do ra none

    # products = read_json(os.path.join(app.root_path, 'data/products.json'))
    #
    # if cate_id:
    #     products = [p for p in products if p['category_id'] == int(cate_id)]
    #
    # if keyword:
    #     for p in products:
    #         print(p['name'].lower().find(keyword.lower()))
    #     products = [p for p in products if p['name'].lower().find(keyword.lower()) >= 0]
    #
    # if from_price:
    #     products = [p for p in products if p['price'] >= float(from_price)]
    #
    # if to_price:
    #     products = [p for p in products if p['price'] <= float(to_price)]

    # return products

def product_detail(product_id):
    return Product.query.get(product_id)
    # products = read_json(os.path.join(app.root_path, 'data/products.json'))
    # for p in products:
    #     if p["id"] == product_id:
    #         return p

"""
Lay toan bo danh sach san pham con active
.count = select count(*) from products
"""
def count_products():
    return Product.query.filter(Product.active.__eq__(True)).count()

"""
Thuc hien dang ky user
"""
def add_user(name, username, password, **kwargs):
    # bam password sau do moi luu vao CSDL
    # .strip() : xoa khoang trang 2 dau
    password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                email=kwargs.get('email'),
                avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

"""
check dang nhap, chu y password dang ky ma hoa the nao thi check cung nhu vay
"""
def check_login(username, password):
    if username and password:
        password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

"""
Tao ham count chua cac thong tin ve so luong, don gia
"""
def count_cart(cart):
    total_quantity, total_amount = 0, 0
    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

        result = {
            'total_quantity': total_quantity,
            'total_amount': total_amount
        }
    return result