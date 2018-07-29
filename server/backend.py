from flask import Flask, request
from flask_restful import Resource, Api
from google.oauth2 import id_token
from google.auth.transport import requests
from objdict import ObjDict
import sqlite3
import json

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        try:
            # google auth
            # request = requests.Request()
            login_token = request.form['login_token']
            print('login token received: ' + login_token)
            id_info = id_token.verify_oauth2_token(
                login_token, requests.Request(), '592019730220-i4op0q91nquh8hoeccreoui2pvvhjr6d')
            if id_info['iss'] != 'https://accounts.google.com':
                print('iss received: ' + id_info)
                raise ValueError('Wrong issuer.')
            user_id = id_info['sub']
            user_email = id_info['email']
            user_name = id_info['name']
            conn = sqlite3.connect('C:\sqlite\praxis.db')
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE user_id = {0} and name = {1} and email = {2} and activated = 1'.format(user_id, user_name, user_email))
            print(c.fetchone)

        except ValueError:
            msg = "something was wrong with the token"
            print(msg)
            return {'error' : msg}


api.add_resource(Login, '/api/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
