from . import db

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True) # 
    stu_id = db.Column(db.Integer, unique=True, nullable=False)
    stu_name = db.Column(db.String(32), unique=True, nullable=False)
    stu_class = db.Column(db.Integer)

class 