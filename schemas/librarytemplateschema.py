from config import ma, db
from models.librarymodel import Library
from schemas.templetschema import TemplateSchema


class LibraryTemplateSchemas(ma.ModelSchema):
   templates = ma.Nested(TemplateSchema, many=True)
   class Meta:
       model = Library
       fields = ("id", "Libaray_Reference", "Title",
                 "Segment", "Section", "Area",
                 "Risk", "Review_Categorisation", "Control_Step",
                 "Audit_Objective", "Document_Sort_No",
                 "Master_Data", "Guidance", "createdby", "templates", "Comments")
       sqla_session = db.session
