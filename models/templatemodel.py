import datetime
from config import db


class Templates(db.Model):
    __tablename__ = "templates"
    id = db.Column(db.Integer, primary_key=True)
    Template_Title = db.Column(db.String(255), nullable=False)
    Template_File = db.Column(db.String(255), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime)
