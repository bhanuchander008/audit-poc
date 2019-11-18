from config import ma, db
from models.librarymodel import Library
from schemas.userschema import UserlibrarySchema
# from schemas.templetschema import TemplateSchema


class LibraryUserSchema(ma.ModelSchema):
   user_updated = ma.Nested(UserlibrarySchema, many=True)
   user_created = ma.Nested(UserlibrarySchema, many=True)
#    templates = ma.Nested(TemplateSchema, many=True)

   class Meta:
       model = Library
       fields = ("id", "Libaray_Reference", "user_updated", "user_created",
                 "Version_id", "created_at", "updated_at")
       sqla_session = db.session
