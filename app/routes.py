from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from __init__ import app
from models import Teacher
db = SQLAlchemy(app)
@app.route('/index')
@app.route('/')
def index():
    return render_template('home.html')
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
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/add')
def add():
    name = "abudllah"
    lastname = "Hussaini"
    age = 23
    try:
        teacher = Teacher(name,lastname,23)
