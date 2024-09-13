"""
Tao doi tuong admin => cung add app vao
"""
from saleapp import app
from flask_admin import Admin
"""
"""
from flask_admin.contrib.sqla import ModelView
"""
chay cai nay se tao trang admin => qua index add trang admin vao
"""
admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4')
