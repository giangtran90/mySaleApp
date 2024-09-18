"""
Tao doi tuong admin => cung add app vao
"""
from saleapp import app,db
from flask_admin import Admin, BaseView, expose, AdminIndexView
"""
moi model se tao 1 trang cho minh
"""
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category,Product,UserRole
from flask_login import current_user, logout_user
from flask import redirect
import utils

class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

"""
muon custom lai 1 view ta ke thua tu ModelView
Trong Model view ta muon cau hinh cai gi thi chi viec lay ra va cau hinh
"""
class ProductView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True # cho phep hien thi detail san pham
    can_export = True # cho phep export ra file excel
    column_searchable_list = ('name', 'description') # them search vao
    column_filters = ('name', 'price')
    column_exclude_list = ('image', 'active', 'created_date')
    column_labels = {
        'name': 'Ten san pham',
        'description': 'Mo ta',
        'price': 'Gia',
        'image': 'Anh',
        'category': 'Danh muc'
    }
    column_sortable_list = ['name', 'id', 'price']

"""
    Logout se ke thua mot BaseView
    expose: giup khi bam vao no logout
"""
class LogoutView(BaseView):
    @expose('/')
    def __index__(self):
        logout_user()
        return redirect('/admin')

    """
        dang nhap vao moi thay logout
    """
    def is_accessible(self):
        return current_user.is_authenticated

class MyAdminIndex(AdminIndexView):
    @expose('/')
    def __index__(self):
        return self.render('admin/index.html', stats=utils.category_stats())

"""
chay cai nay se tao trang admin => qua index add trang admin vao
"""
admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4', index_view=MyAdminIndex())

"""
Them cac view vao cho trang admin
"""
admin.add_view(AuthenticatedModelView(Category,db.session))
admin.add_view(ProductView(Product,db.session))
admin.add_view(LogoutView(name='Logout'))
