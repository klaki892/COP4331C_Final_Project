from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from endpoints.test import *
from endpoints.users import *
from database.db import  getSession

app = Flask(__name__)
app.config.from_pyfile('api.cfg')
api = Api(app)

api.add_resource(TestEndpoint, '/test')
api.add_resource(DbTestEndpoint, '/dbTest')
api.add_resource(UserRegisterEndpoint, '/register')

if __name__ == '__main__':
    app.run(debug=False, port=8080)