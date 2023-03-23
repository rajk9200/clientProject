from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


from flask_marshmallow import Marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/myproject1'
db = SQLAlchemy(app)
api =Api(app)
ma = Marshmallow(app)
from myapp import routes





