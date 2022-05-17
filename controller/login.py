from flask import Blueprint, Flask, render_template, jsonify, request, make_response
from database import db
import jwt
import datetime

SECRET_KEY = 'SECRET_KEY'

login_blueprint = Blueprint(
    'login_blueprint', __name__, template_folder='templates')


@login_blueprint.route("/login")
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm="HS256")

        return jsonify({'token': token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
