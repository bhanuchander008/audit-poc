from config import ma,db
from models.rolemodel import Roles
from models.usermodel import Users
from marshmallow import fields
from marshmallow.fields import Nested
from schemas.roleschema import RolesGetSchema

class UsersGetSchema(ma.ModelSchema):
    Role_User = ma.Nested(RolesGetSchema)
    class Meta:
        model =Users
        fields = ("id","first_name","last_name","phone","gender","address","status","email","Role_User")
        sqla_session = db.session

class UsersSchema(ma.ModelSchema):
    class Meta:
        models = Users
        fields = ("id","first_name","last_name","phone","gender","address","status","email","role_id")
        sqla_session = db.session

class user_signupSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ("id", "email", "first_name", "last_name", "phone")
        sqla_session = db.session

class User_loginSchema(ma.ModelSchema):
    Role_User = ma.Nested(RolesGetSchema)
    class Meta:
        model = Users
        fields = ("id", "email", "Role_User", "first_name", "last_name", "phone")
        sqla_session = db.session


class GetallUsersSchemas(ma.ModelSchema):
    Role_User = ma.Nested(RolesGetSchema)
    class Meta:
        models = Users
        fields = ("id", "first_name", "last_name",
                  "phone", "email", "Role_User")
        sqla_session = db.session


class UserlibrarySchema(ma.ModelSchema):
   class Meta:
       models = Users
       fields = ("first_name", "last_name")
       sqla_session = db.session
# class Password_ResetSchema(ma.ModelSchema):
#     class Meta:
#         model = Users
#         fields = ("password",)
#         sqla_session = db.session
#
#
# class UserlogoutSchema(ma.ModelSchema):
#     class Meta:
#         model = RevokedTokenModel
#         sqla_session = db.session
#
# class UserOrderSchema(ma.ModelSchema):
#     class Meta:
#         model = Users
#         fields = ("id","name","username")
#
# class UsercountSchema(ma.ModelSchema):
#     Role_user  = ma.Nested(RoleSchema)
#     class Meta:
#         model = Users
#         fields = ("id","name","username","mobileNumber","roleId","Role_user")
#
# class UseraccountSchema(ma.ModelSchema):
#     Role_user  = ma.Nested(RoleSchema)
#     class Meta:
#         model = Users
#         fields = ("id","name","username","mobileNumber","roleId","Role_user")
#
#
# class UsersSchemas(ma.ModelSchema):
#     class Meta:
#         models = Users
#         fields = ("id","name","mobileNumber","username","address")
#         sqla_session = db.session
