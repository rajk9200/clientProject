from myapp import api
from myapp import views

api.add_resource(views.get,'/getStudent')