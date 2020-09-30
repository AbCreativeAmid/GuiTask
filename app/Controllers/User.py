import routes
from app import app
from flask import render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from models import *
import time
import os
from werkzeug.security import generate_password_hash
db = SQLAlchemy(app)
class User_controller:
    @staticmethod
    def add(request):
        global db
        email      = request.form['email']
        password   = generate_password_hash(request.form['password'])
        username   = request.form['username']
        photo      = request.files['photo']
        role       = request.form['role']
        if(int(request.form['id'])!=-1):
            try:
                user = User.query.get(request.form['id'])
                user.email = email
                user.password = password
                user.username = username
                user.role = int(role)
                user.updated_at = round(time.time())
                if photo.filename != '':
                    oldphoto = user.photo
                    assets_dir = os.path.join(
                    os.path.dirname(app.instance_path), 'static/images/'
                    )
                    newname = str(round(time.time()))+"user.jpg"
                    photo.save(os.path.join(assets_dir,'users/',newname))
                    user.photo = assets_dir+'users/'+newname
                db.session.commit()
                if photo.filename != '':
                    os.unlink(oldphoto)
                return redirect('/users')
            except Exception as e:
                return (str(e))
        else:
            try:
                nuser = User(username=username,status=0,last_seen=0,password=password,email=email,role=role,photo="null",created_at=round(time.time()),updated_at=round(time.time()))
                if photo.filename != '':
                    assets_dir = os.path.join(
                    os.path.dirname(app.instance_path), 'static/images/'
                    )
                    newname = str(round(time.time()))+"user.jpg"
                    photo.save(os.path.join(assets_dir,'users/',newname))
                    nuser.photo = assets_dir+'users/'+newname
                db.session.add(nuser)
                db.session.commit()
                return redirect ('/users')
            except Exception as e:
                return (str(e))

class Product_controller:
    @staticmethod
    def add(request):
        global db
        name      = request.form['name']
        quantity   = request.form['quantity']
        price   = request.form['price']
        discount   = request.form['discount']
        photo      = request.files['photo']
        category = request.form['category']
        if int(request.form['id'])!=-1:
            try:
                product = db.session.query(Product).get(request.form['id'])
                product.name = name
                product.quantity = quantity
                product.price = price
                product.discount = discount
                product.category = category
                product.updated_at = round(time.time())
                if photo.filename != '':
                    oldphoto = product.photo
                    assets_dir = os.path.join(
                    os.path.dirname(app.instance_path), 'static/images/'
                    )
                    newname = str(round(time.time()))+"product.jpg"
                   
                    photo.save(os.path.join(assets_dir,'products/',newname))

                    product.photo = assets_dir+'products/'+newname
              
                db.session.commit()
                if photo.filename != '':
                    os.unlink(oldphoto)
                flash("Successfully updated!")
                return redirect('/products')
            except Exception as e:
                return (str(e))
        else:
            try:
                nproduct = Product(name=name,quantity=quantity,price=price,discount=discount,category=category,photo="null",created_at=round(time.time()),updated_at=round(time.time()))
                if photo.filename != '':
                    assets_dir = os.path.join(
                    os.path.dirname(app.instance_path), 'static/images/'
                    )
                    newname = str(round(time.time()))+"product.jpg"
                    photo.save(os.path.join(assets_dir,'products/',newname))
                    nproduct.photo = assets_dir+'products/'+newname
                db.session.add(nproduct)
                db.session.commit()
                return redirect ('/products')
            except Exception as e:
                return (str(e))    
