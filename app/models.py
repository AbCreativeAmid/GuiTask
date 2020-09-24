from __init__ import db
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    age = db.Column(db.Integer)
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'lastname':self.lastname,
            'age':self.age
        }