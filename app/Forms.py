from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField, SubmitField,FileField,SelectField,IntegerField,TextField
from wtforms.validators import DataRequired,Length,EqualTo,Email,NumberRange
from wtforms import validators
from wtforms.fields import html5 as h5fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets import html5 as h5widgets
from models import Category
class AddUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=5,max=20,message="must be between 5 to 20 characters")])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('rpassword',message="Password must match!")])
    rpassword = PasswordField('Repeat Password', validators=[DataRequired()])
    role = SelectField("Role",choices=[('1','Admin'),('2','Manager')],validators=[DataRequired()])
    photo = FileField("Photo")
    email = StringField('Email',validators =[DataRequired(),Email()])
    submit = SubmitField('Submit')
class AddProduct(FlaskForm):
    name = StringField('name', validators=[DataRequired(),Length(min=5,max=20,message="must be between 5 to 20 characters")])
    quantity = IntegerField('quantity(kg)',validators=[NumberRange(min=1 ,max = 100000,message="quantity must be between 1 to 100000"),DataRequired()])
    price = IntegerField('price(per kg)',validators=[NumberRange(min=1 ,max = 100000,message="price must be between 1 to 100000"),DataRequired()])
    discount = IntegerField('discount(per kg)',validators=[NumberRange(min=1 ,max = 100000,message="discount must be between 1 to 100000")])
    category = QuerySelectField('category',query_factory=lambda:Category.query.all(),get_label="name")
    photo = FileField("Photo")
    submit = SubmitField('Submit')
class AddPost(FlaskForm):
    title = StringField('title', validators=[DataRequired(),Length(min=5,max=20,message="must be between 5 to 20 characters")])
    author = StringField('author', validators=[DataRequired(),Length(min=3,max=20,message="must be between 3 to 20 characters")])
    text = TextField('text',validators=[DataRequired(),Length(min=100,max=50000,message="must be between 100 to 50000 characters")])
    photo = FileField("Photo")
    submit = SubmitField('Submit')
