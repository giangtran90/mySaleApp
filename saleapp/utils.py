import json, os
from itertools import product

from unicodedata import category

from saleapp import app

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
  doc tuyet doi : nen dung bang cach import them os va app
"""
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products(cate_id=None, keyword=None, from_price=None, to_price=None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]

    if keyword:
        for p in products:
            print(p['name'].lower().find(keyword.lower()))
        products = [p for p in products if p['name'].lower().find(keyword.lower()) >= 0]

    if from_price:
        products = [p for p in products if p['price'] >= float(from_price)]

    if to_price:
        products = [p for p in products if p['price'] <= float(to_price)]

    return products

def product_detail(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))
    for p in products:
        if p["id"] == product_id:
            return p