from flask_restful import Resource
from flask import Flask, request, jsonify,Response
from myapp.models import Subjects,Groups,Student
from myapp import db
from serializer import people_schema, person_schema
class Subject(Resource):
    def get(self):
        context = {}
        s=Subjects.query.all()
        res=people_schema.dump(s)
        print(res)
        context['list']=res
        return jsonify(context)
    def post(self):
        context={}
        try:
            title=request.json.get('title')
            s=Subjects(title=title)
            db.session.add(s)
            db.session.commit()
            context['message']=f"{title} subject added successfully."
        except:
            context['error']="Subject adding problem."

        return jsonify(context)
    def put(self):
        context={}
        try:
            subject_id=request.json.get('subject_id')

            try:
                s=Subjects.query.filter_by(subject_id=int(subject_id)).update(dict(title='Math'))
                db.session.commit()
                context['message'] = f"{s.title} subject Update successfully."
            except Exception as e:
                context['message']=f"{e} subject_id id not matched"
        except:
            context['error']="Subject adding problem."

        return jsonify(context)
    def delete(self):
        context={}
        try:
            title=request.json.get('title')
            s=Subjects.query.filter_by(title=title).first()
            db.session.delete(s)
            db.session.commit()
            context['message']=f"{title} subject deleted successfully."
        except Exception as e:
            context['error']=f"{e} Subject deleted problem."

        return jsonify(context)


