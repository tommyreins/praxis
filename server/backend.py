from flask import Flask
from flask_restful import Resource, Api
from objdict import ObjDict
import sqlite3
import json

app = Flask(__name__)
api = Api(app)

class TReiner(Resource):
      def get(self):
            conn = sqlite3.connect('backend.db')
            c = conn.cursor()
            
            c.execute("SELECT * FROM TASKS")
            colnames = c.description
            col_str = ""
            for row in colnames:
                  col_str += (row[0] + " ")
            col_str = col_str.split(" ")
            data = ObjDict()
            i = 0
            for row in c.fetchall():
                  parsed_id = 0
                  id = -1
                  sub_dict = {}
                  for elem, col in zip(row, col_str):
                        if parsed_id is 0:
                              id = str(elem)
                              parsed_id = 1
                        else:
                              sub_dict[col] = elem
                  data[id] = sub_dict
            return data

api.add_resource(TReiner, '/')

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')

