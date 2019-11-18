from config import ma,db
from models.rolemodel import Roles


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Roles
        #fields = ("id","role","status","created_at","updated_at","User")
        sqla_session = db.session


class RolesGetSchema(ma.ModelSchema):
    class Meta:
        model = Roles
        fields = ("id","role")
        sqla_session = db.session
