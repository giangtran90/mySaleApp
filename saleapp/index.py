import math

from flask import render_template, request, redirect, url_for

from saleapp import app
import utils


@app.route("/")
def home():
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
    return render_template('index.html', products = products, pages = math.ceil(counter/app.config['PAGE_SIZE']))

"""
register co 2 methode la get, post de lay thong tin va dang ki thong tin
"""
@app.route('/register', methods = ['get', 'post'])
def user_register():
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        """
        thuc hien xac nhan, neu mat khau nhap va xac nhan mat khau dung thi moi thuc hien add con neu khong thi se tra ra loi
        """
        try:
            if password.strip().__eq__(confirm.strip()):
                utils.add_user(name=name,username=username,password=password,email=email)
                return redirect(url_for('home'))
            else:
                err_msg = 'Mat khau khong trung nhau!!!'
        except Exception as ex:
            err_msg = 'Loi he thong!!!' + str(ex)

    return render_template('register.html', err_msg=err_msg)

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

"""
su dung @app.context_processor: de no tu dog ap categories vao tat ca cac trang
"""
@app.context_processor
def common_response():
    return {
        "categories" : utils.load_categories()
    }

if __name__ == '__main__':
    """
    import admin vao de khi chay no render ra trang admin
    """
    from saleapp.admin import *

    app.run(debug=True)