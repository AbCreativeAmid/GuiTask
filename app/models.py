from app import db
class Product(db.Model):
    __tablename__ = 'products'
    id         = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name       = db.Column(db.String)
    photo      = db.Column(db.String)
    quantity   = db.Column(db.Integer)
    price      = db.Column(db.Integer)
    discount   = db.Column(db.Integer)
    category   = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,name,photo,quantity,price,discount,category,created_at,updated_at):
        self.name = name
        self.photo= photo
        self.quantity = quantity
        self.price = price
        self.discount= discount
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'photo':self.photo,
            'quantity':self.quantity,
            'price':self.price,
            'discount':self.discount,
            'category':self.category,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    photo = db.Column(db.String)
    status = db.Column(db.Integer)
    role = db.Column(db.Integer)
    last_seen = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,username,password,email,role,status,last_seen,photo,created_at,updated_at):
        self.username = username
        self.password =password
        self.email = email
        self.photo = photo
        self.role = role
        self.status = status
        self.last_seen = last_seen
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'password':self.password,
            'email':self.email,
            'role':self.role,
            'photo':self.photo,
            'status':self.status,
            'last_seen':self.last_seen,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    author = db.Column(db.Integer)
    photo = db.Column(db.String)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,title,text,photo,author,created_at,updated_at):
        self.title = title,
        self.text = text,
        self.author = author
        self.photo = photo
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'title':self.title,
            'text':self.text,
            'author':self.author,
            'photo':self.photo,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }

class Sale(db.Model):
    __tablename__ = 'sales'
    id         = db.Column(db.Integer,primary_key=True,autoincrement=True)
    bill       = db.Column(db.String)
    price      = db.Column(db.Integer)
    c_name      = db.Column(db.String)
    address     = db.Column(db.String)
    phone       = db.Column(db.String)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,bill,price,c_name,address,phone,created_at,updated_at):
        self.bill = bill
        self.price= price
        self.c_name = c_name
        self.phone = phone
        self.address = address
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'bill':self.bill,
            'price':self.price,
            'c_name':self.c_name,
            'address':self.address,
            'phone':self.phone,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }

class Sale_Item(db.Model):
    __tablename__ = 'sales_items'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    product_id  = db.Column(db.Integer)
    price       = db.Column(db.Integer)
    quantity   = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,product_id,quantity,price,created_at,updated_at):
        self.product_id = product_id
        self.price= price
        self.quantity= quantity
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'product_id':self.product_id,
            'quantity':self.quantity,
            'price':self.price,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer)
    text = db.Column(db.String)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    def __init__(self,post_id,text,created_at,updated_at):
        self.post_id = post_id
        self.text = text
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'post_id':self.post_id,
            'text':self.text,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }
class Category(db.Model):
    __tablename__ = 'categories'
    id         = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name       = db.Column(db.String)
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name
        }