from app import app
from API import login_register
from flask import make_response
from flask import jsonify
from app import db
from flask import request
from flask import Flask

def response():
    def success(values,message='success'):
        res = {
            'data': values,
            'message': message
        }
        return make_response(jsonify(res), 200)

    def badRequest(values,message='success'):
        res = {
            'data': values,
            'message': message
        }
        return make_response(jsonify(res), 400)

@app.route('/')
def index():
    return 'Hello Flask!! its Work!!'

@app.route('/showUser', methods=['GET'])
def showUser():
    return login_register.showUser()

@app.route('/login', methods=['POST'])
def login():
    return login_register.login()

@app.route('/register', methods=['POST'])
def register():
    return login_register.register()



