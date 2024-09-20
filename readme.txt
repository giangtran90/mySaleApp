Template Flask sử dụng Jinja2 để đánh dấu các thẻ template.
Hoc kien thuc co ban ve flask trong python qua du an web
- kien thuc python co ban
- tao web don gian ket noi voi json
	kich hoat flask: pip install flask
- thuc hien ket noi du lieu bang mysql thong qua sqlAlchemy cua Flask
    Can cai dat: pip install flask-sqlalchemy pymysql
    branch: 20240912_flask_sqlalchemy
- thuc hien tao trang admin bang flask-admin duoc ho tro san
    pip install flask-admin
    branch: 20240913_create_admin_page
- tao mot trang base.html dung chung cau hinh cho file do de sau ke thua lai template
    tao cac block de sau chi viec ke thua lai
- tao chuc nang phan trang Flask SqlAlchemy
    branch: 20240914_pagination
- tao dang ky nguoi dung va upload anh len web
  + upload anh vao cloudinary : pip install coudinary
    branch: 20240917_crud_user
- Xu ly dang nhap nguoi dung
    cai plugin login de no tu ghi nhan trang thai dang nhap: pip install flask-login
    => de su dung, dau tin tao 1 bien login o _init_ => trong models thi them UserMixin => utils: get_user_by_id
    => index: user_load voi @login.user_loader() se tu goi khi no dang nhap thanh cong => import login_user tu flask-login
    => login_user(user=user) giup ghi nhan trang thai dang nhap va bo vao current_user
    branch: 20240917_user_login
- Tao chuc nang gio hang : flask session
    + xay dung chuc nang gio hang va ghi nhan don hang
    branch: 20240917_flask_session_gio_hang
- Flask-admin: Tuy chinh template Trang chu va thuc hien dang nhap voi flask-login
- Flask-admin: Tuy chinh trang chu admin voi thong ke san pham theo danh muc va ve bieu do chartjs
    co nhieu thu vien ve bieu do nhu goodlejs, o day dung chartjs.org
    branch: feature/20240918_edit_page_admin
- Xay dung chuc nang thong ke bao cao doanh thu va ve bieu do bang chartjs
  Tuong tu thong ke theo thang va ve bieu do
  branch: feature/20240919_bao_cao_doanh_thu
- Thuc hien chuc nang cap nhat gio hang dung Ajax
  Thuc hien xoa san pham cung su dung Ajax
  branch: feature/20240919_chuc_nang_cap_nhat_gio_hang
- Tao trang chi tiet san pham va thuc hien chuc nang binh luan
  Thuc hien phan trang bang cach nap load lai trang: dung thu vien momentjs de chuyen ngay thang dang binh luan
  branch: feature/20240919_chi_tiet_sp_binh_luan