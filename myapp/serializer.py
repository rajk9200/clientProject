from myapp import db, ma

from myapp import models

class SubjectSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Subjects
        load_instance = True
        sqla_session = db.session


person_schema = models.Subjects()
people_schema = SubjectSerializer(many=True)