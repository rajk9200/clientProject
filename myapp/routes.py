from myapp import app

from myapp import db
@app.route('/')
def index():
    return "welcome to my website"
# subjects crud
@app.route('/create_tables')
def ctables():
    db.create_all()
    return "Table Created Successfully.."


from myapp import api
from myapp import views

api.add_resource(views.Subject,'/api/vi/Student')



