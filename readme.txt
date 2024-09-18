
Hoc kien thuc co ban ve flask trong python qua du an web
- kien thuc python co ban
- tao web don gian ket noi voi json
	kich hoat flask: pip install flask
- thuc hien ket noi du lieu bang mysql thong qua sqlAlchemy cua Flask
    Can cai dat: pip install flask-sqlalchemy pymysql
- thuc hien tao trang admin bang flask-admin duoc ho tro san
    pip install flask-admin
- tao mot trang base.html dung chung cau hinh cho file do de sau ke thua lai template
    tao cac block de sau chi viec ke thua lai
- tao chuc nang phan trang Flask SqlAlchemy
- tao dang ky nguoi dung va upload anh len web
  +upload anh vao cloudinary : pip install coudinary
- Xu ly dang nhap nguoi dung
    cai plugin login de no tu ghi nhan trang thai dang nhap: pip install flask-login
    => de su dung, dau tin tao 1 bien login o _init_ => trong models thi them UserMixin => utils: get_user_by_id
    => index: user_load voi @login.user_loader() se tu goi khi no dang nhap thanh cong => import login_user tu flask-login
    => login_user(user=user) giup ghi nhan trang thai dang nhap va bo vao current_user
- Tao chuc nang gio hang : flask session
    + xay dung chuc nang gio hang va ghi nhan don hang
- Flask-admin: Tuy chinh template Trang chu va thuc hien dang nhap voi flask-login