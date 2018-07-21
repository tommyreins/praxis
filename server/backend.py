from flask import Flask
from flask_restful import Resource, Api
from objdict import ObjDict
import sqlite3
import json

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def GET(self):
        conn = sqlite3.connect('C:\sqlite\praxis.db')
        c = conn.cursor()


api.add_resource(TReiner, '/login/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
