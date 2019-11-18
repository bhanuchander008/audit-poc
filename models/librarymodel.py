import datetime
from sqlalchemy.orm import relationship
from config import db
from models.templatemodel import Templates

class Library(db.Model):
    __tablename__ = "library"
    id                    = db.Column(db.Integer, primary_key=True)
    Libaray_Reference     = db.Column(db.String(255), nullable=False, unique=True)
    Version_id            = db.Column(db.String(255), nullable=True)
    Title                 = db.Column(db.String(255), nullable=False)
    Segment               = db.Column(db.String(255), nullable=False)
    Section               = db.Column(db.String(255), nullable=False)
    Area                  = db.Column(db.String(255), nullable=False)
    Risk                  = db.Column(db.String(255), nullable=False)
    Review_Categorisation = db.Column(db.String(255), nullable=False)
    Control_Step          = db.Column(db.Boolean, default = True)
    Audit_Objective       = db.Column(db.String(255), nullable=False)
    Document_Sort_No      = db.Column(db.String(255), nullable=False)
    Master_Data           = db.Column(db.String(255), nullable=False)
    Guidance              = db.Column(db.Text(), nullable=True)
    status                = db.Column(db.Boolean, default = True)
    Template              = db.Column(db.Boolean, default = True)
    Comments              = db.Column(db.String(255), nullable=True)
    updatedby             = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = True)
    createdby             = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    created_at            = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at            = db.Column(db.DateTime)

    templates = db.relationship("Templates", backref=db.backref('templates'), uselist=True)
    user_updated = db.relationship("Users",  backref=db.backref('user_updated'), foreign_keys="[Library.updatedby]", uselist=True)
    user_created = db.relationship("Users",  backref=db.backref('user_created'), foreign_keys="[Library.createdby]",uselist=True)
