import json, os

from unicodedata import category

from saleapp import app
from saleapp.models import Category, Product, products

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

def load_products(cate_id=None, keyword=None, from_price=None, to_price=None):
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

    return products.all() # them .all de neu khong co la no se do ra none

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