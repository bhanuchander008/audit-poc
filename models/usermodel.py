import datetime
from sqlalchemy.orm import relationship
from config import db
from models.librarymodel import Library

class Users(db.Model):
    __tablename__ = "users"
    id             = db.Column(db.Integer,primary_key=True)
    first_name     = db.Column(db.String(255),nullable=True)
    last_name      = db.Column(db.String(255),nullable = True)
    phone          = db.Column(db.String(255),nullable = True)
    email          = db.Column(db.String(120), unique = True, nullable = False)
    password       = db.Column(db.String(255))
    address        = db.Column(db.Text(),nullable = True)
    gender         = db.Column(db.Enum('M','F','O'),nullable=True)
    role_id        = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = True)
    status         = db.Column(db.Boolean, default = True)
    created_at     = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at     = db.Column(db.DateTime)
