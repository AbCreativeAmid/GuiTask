import routes
from app import app
from flask import render_template,request,redirect,flash,session
from flask_sqlalchemy import SQLAlchemy
from models import *
import time
import os
from werkzeug.security import generate_password_hash

class Login:
    db = SQLAlchemy(app)
    @staticmethod
    def login(username,password):
        user = db.session.query(User).filter(User.username== username and User.password == generate_password_hash(password)).first()
        if not user:
            return False
        else:
            session['login'] = {'id':user.id,'username':user.username,'role':user.role,'login':True}
            try:
                user.status = 1
                db.session.commit()
            except:
                return False
            return True
    @staticmethod
    def logout():
        try:
            user = db.session.query(User).get(session.get('login')['id'])
           
            user.status = 0
            user.last_seen = round(time.time())
            db.session.commit()
        except:
            return False
        session.pop('login',None)
        return True
