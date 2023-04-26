from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/put-book')
def put_book():
    return render_template('put_book.html')

@views.route('/my-book')
def my_book():
    return render_template('my_book.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@views.route('/<catalogs>')
def catalogs(catalogs):
    return render_template('catalogs.html', catalogs={catalogs})

catalogs = [
    'giao-trinh-noi', 'noi-tong-quat', 'noi-ho-hap', 'noi-tim-mach', 'noi-tieu-hoa', 
    'noi-than-tiet-nieu', 'noi-tiet', 'noi-co-xuong-khop', 'noi-than-kinh',
    'di-ung-mien-dich', 'hoi-suc-cap-cuu-icu', 'huyet-hoc-truyen-mau', 
    'giao-trinh-ngoai', 'ngoai-tong-quat', 'ngoai-cap-cuu', 'ngoai-tieu-hoa', 'ngoai-long-nguc', 
    'ngoai-mach-mau', 'ngoai-tiet-nieu', 'ngoai-than-kinh', 'chan-thuong-chinh-hinh', 'bong', 
    'giao-trinh-san-phu-khoa', 'san-khoa', 'phu-khoa', 
    'giao-trinh-nhi-khoa', 'noi-nhi', 'ngoai-nhi', 
    'nhan-khoa', 'da-lieu', 'tai-mui-hong', 'rang-ham-mat', 'truyen-nhiem', 'lao', 
    'ung-buou', 'tam-than', 'huyen-hoc', 'lao-khoa', 'nam-khoa', 'gay-me-hoi-suc', 
    'phuc-hoi-chuc-nang', 'y-hoc-co-truyen', 'y-te-cong-cong', 
    'ky-nang-lam-sang', 'di-truyen-hoc', 'duoc-ly-hoc', 'giai-phau-benh', 'giai-phau-hoc',
    'hoa-hoc', 'hoa-sinh-hoc', 'mo-phoi', 'sinh-hoc-shpt', 'sinh-ly-benh-mien-dich', 
    'sinh-ly-hoc', 'tam-ly-hoc', 'toan-tin-nckh', 'tieng-anh-y-khoa', 'vat-ly-ly-sinh', 
    'vi-sinh-ky-sinh-trung', 'y-te-cong-cong', 
    'chan-doan-hinh-anh', 'xet-nghiem', 'dien-tam-do', 'dien-nao-do', 
    'dieu-duong', 'duoc-hoc'
]

