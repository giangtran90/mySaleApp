import math

from flask import render_template, request, redirect, url_for, session, jsonify

from saleapp import app, login
import utils
import cloudinary.uploader # de ho tro upload anh
from flask_login import login_user, logout_user, login_required


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
        avatar_path = None
        """
        thuc hien xac nhan, neu mat khau nhap va xac nhan mat khau dung thi moi thuc hien add con neu khong thi se tra ra loi
        """
        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar') # chu y la files chu ko phai form
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url'] # chu y res['secure_url'] lay duong dan flask cloudinary response data
                utils.add_user(name=name,username=username,password=password,email=email, avatar=avatar_path)
                return redirect(url_for('user_signin'))
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
tao link ket noi trang cart
"""
@app.route('/cart')
def cart():
    return render_template('cart.html')

"""
tao add cart
"""
@app.route('/api/add-cart', methods=['post'])
def add_to_cart():
    data = request.json
    id = str(data.get('id'))
    name = data.get('name')
    price = data.get('price')

    """lenh debug=> chay toi se dung lai cho minh debug"""
    # import pdb
    # pdb.set_trace()

    cart = session.get("cart") # lay cart
    if not cart:
        cart = {}
    if id in cart:
        cart[id]['quantity'] = cart[id]['quantity'] + 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1
        }

    session['cart'] = cart
    """
    jsonify dung de chuyen doi sang dang json
    """
    strResultCart = jsonify(utils.count_cart(cart))
    return strResultCart

"""Chuc nang tra tien dung js xu ly"""
@app.route('/api/pay', methods = ['post'])
@login_required
def pay():
    try:
        utils.add_receipt(session.get('cart'))
        del session['cart'] # sau khi thanh toan no se xoa session
    except:
        return jsonify({'code': 400})
    return jsonify({'code': 200})

"""
chuc nang dang nhap
"""
@app.route('/user-login', methods=['get','post'])
def user_signin():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = utils.check_login(username=username, password=password)
        if user:
            """Luc nay da co bien toan duc global current_user bang cach goi login_user"""
            login_user(user=user)
            next = request.args.get('next', 'home') # neu args co next thi lay next khong thi se lay home
            return redirect(url_for(next))
        else:
            err_msg = 'username hoac password khong dung!!!'
    return render_template('login.html', err_msg=err_msg)

@app.route('/user-logout')
def user_signout():
    logout_user() # chi viec goi no se tu dong xoa plugin tich hop san
    return redirect(url_for('user_signin'))

"""
su dung @app.context_processor: de no tu dog ap categories vao tat ca cac trang
"""
@app.context_processor
def common_response():
    return {
        "categories" : utils.load_categories(),
        "cartStat": utils.count_cart(session.get('cart'))
    }

"""
@login.user_loader() se tu goi khi no dang nhap thanh cong
"""
@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

if __name__ == '__main__':
    """
    import admin vao de khi chay no render ra trang admin
    """
    from saleapp.admin import *

    app.run(debug=True)