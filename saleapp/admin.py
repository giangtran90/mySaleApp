"""
Tao doi tuong admin => cung add app vao
"""
from saleapp import app,db
from flask_admin import Admin
"""
moi model se tao 1 trang cho minh
"""
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category,Product
"""
chay cai nay se tao trang admin => qua index add trang admin vao
"""
admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4')

"""
muon custom lai 1 view ta ke thua tu ModelView
Trong Model view ta muon cau hinh cai gi thi chi viec lay ra va cau hinh
"""
class ProductView(ModelView):
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

admin.add_view(ModelView(Category,db.session))
admin.add_view(ProductView(Product,db.session))
