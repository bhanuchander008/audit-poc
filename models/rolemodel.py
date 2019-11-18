import datetime
from sqlalchemy.orm import relationship
from config import db
from models.usermodel import Users


class Roles(db.Model):
    __tablename__ = "roles"
    id         = db.Column(db.Integer,primary_key=True)
    role       = db.Column(db.String(50),nullable=True)
    status     = db.Column(db.Boolean, default = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime)
    User = db.relationship("Users", backref=db.backref("Role_User"), uselist=True)
