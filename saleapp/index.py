import math

from flask import render_template, request
from saleapp import app
import utils
from saleapp.models import products


@app.route("/")
def home():
    cates = utils.load_categories()
    cate_id = request.args.get("category_id")
    keyword = request.args.get("keyword")
    """
    them vao args page => thuc hien phan trang
    chu y la ep qua kieu so nguyen
    """
    page = int(request.args.get("page",1))
    products = utils.load_products(cate_id=cate_id, keyword=keyword, page = page)
    """
    lay tong so trang
    """
    counter = utils.count_products()
    return render_template('index.html', categories = cates, products = products, pages = math.ceil(counter/app.config['PAGE_SIZE']))

@app.route("/products")
def listProduct():
    """
    import request vao de lay gia tri args o ben ngoai truyen vao
    neu co gia tri thi lay dc gia tri cate_id ko thi la none
    """
    cate_id = request.args.get("category_id")
    keyword = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    products = utils.load_products(cate_id=cate_id, keyword=keyword, from_price=from_price, to_price=to_price)
    return render_template('products.html', listP=products)

@app.route("/products/<int:product_id>")
def productDetail(product_id):
    product = utils.product_detail(product_id)
    return  render_template('product_detail.html', product=product)


if __name__ == '__main__':
    """
    import admin vao de khi chay no render ra trang admin
    """
    from saleapp.admin import *

    app.run(debug=True)