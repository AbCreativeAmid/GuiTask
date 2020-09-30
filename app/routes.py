from flask import render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import alias,join
from Controllers.login_manager import Login
from app import app
from models import *
from Forms import *
from Controllers.User import User_controller,Product_controller
import json
import shutil
import time
import os
db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('home.html',products=products)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/blog_single')
def blog_single():
    return render_template('blog-single.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/cart')
def cart():
    if session.get('cartlenght') != None and session.get('cartlenght') > 0:
        cartlist = db.session.query(Product).filter(Product.id.in_(session.get('cartlist'))).all()
        return render_template('cart.html',cartlist=cartlist)
    return render_template('cart.html')
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')
@app.route('/product_single')
def product_single():
    return render_template('product-single.html')
@app.route('/shop')
def shop():
    return render_template('shop.html')
@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

#login process
@app.route('/admin',methods=["POST","GET"])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Login.login(username=username,password=password):
            return redirect('/')
        else:
            return render_template('login.html',error="username or password is invalid")
    return render_template('login.html',error="")
#end login

#**************Products******************#
#products datatable
@app.route('/products')
def products():
    products = db.session.query(Product.id,Product.name,Product.quantity,Product.price,Product.discount,Category.name.label("cname")).filter(Product.category==Category.id)
    return render_template('products.html',products=products)
#end products datatable

#add product route
@app.route('/add_product',methods=['GET','POST'])
def add_product():
    form = AddProduct()
    if request.method == 'POST' and form.validate_on_submit():
        return Product_controller.add(request)
    else:
        return render_template('add_product.html',form=form)
#end product add

#edit product
@app.route('/edit_product/<id>')
def edit_product(id):
    form = AddProduct()
    product = Product.query.get(id)
    return render_template('add_product.html',product=product,form=form)

#**************END Products******************#

#**************END Users******************#
#users datatable
@app.route('/users')
def users():
    users = User.query.all()
    curtime = round(time.time())
    return render_template('users.html',users= users,curtime=curtime)
#end products datatable


@app.route('/add_user',methods=['GET','POST'])
def add_user():
    form = AddUser()
    if request.method == 'POST' and form.validate_on_submit():
        return User_controller.add(request)
    else:
        return render_template('add_user.html',form=form,a = form.validate_on_submit())

#edit user
@app.route('/edit_user/<id>')
def edit_user(id):
    form = AddUser()
    user = User.query.get(id)
    return render_template('add_user.html',user=user,form=form)

#**************END Users******************#


@app.route('/add_post')
def add_post():
    ab =User.query.get(1)
    return ab.username
@app.route('/logout')
def logout():
    if Login.logout():
        return redirect('/admin')
@app.route('/cart_list',methods=['GET','POST'])
def cart_list():
    id = int(request.form['pid'])
    if session.get('cartlist') is None:
        session['cartlist'] = [id]
        session['cartlenght'] = 1
        return '1'
    else:
        cart = session.get('cartlist')
        cart.append(id)
        session['cartlist'] = cart
        session['cartlenght'] = len(cart)
        return str(len(cart))

# @app.route('/sale')
# def sale():
#     name = request.form['name']
#     address = request.form['address']
#     phone = request.form['phone']
#     price = request.form['price']
#     created_at = round(time.time())
#     updated_at = round(time.time())
#     for c in session.get("cartlist"):
#         product = Product.query.get(c)
#         iprice = product.price-product.discount
#         quantity = request.form["quantity_"+str(c)]
#         item = Sale_Item(product_id=product.id,price=price,created_at=created_at,updated_at=updated_at)

        