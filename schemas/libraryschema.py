from config import ma, db
from models.librarymodel import Library



class LibrarySchema(ma.ModelSchema):
    class Meta:
        model = Library
        fields = ("id","Libaray_Reference", "Title",
                  "Segment", "Section", "Area",
                  "Risk", "Review_Categorisation", "Control_Step",
                  "Audit_Objective", "Document_Sort_No",
                  "Master_Data", "Guidance", "createdby", "Comments", "Template")
        sqla_session = db.session


class LibraryGetSchema(ma.ModelSchema):
    class Meta:
        model = Library
        sqla_session = db.session


class LibraryUpdateSchema(ma.ModelSchema):
    class Meta:
        model = Library
        fields = ("id", "Libaray_Reference", "Title",
                  "Segment", "Section", "Area",
                  "Risk", "Review_Categorisation", "Control_Step",
                  "Audit_Objective", "Document_Sort_No",
                  "Master_Data", "Guidance", "createdby", "updatedby", "Comments", "Template", "Version_id", "updated_at", "created_at")
        sqla_session = db.session
