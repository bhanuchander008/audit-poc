from config import ma, db
from models.templatemodel import Templates


class TemplateSchema(ma.ModelSchema):
    class Meta:
        model = Templates
        fields = ("Template_Title", "Template_File", "user_id", "library_id")
        sqla_session = db.session
