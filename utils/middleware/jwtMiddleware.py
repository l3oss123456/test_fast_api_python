from flask import jsonify, request
import jwt
from functools import wraps

SECRET_KEY = 'SECRET_KEY'


def token_requierd(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(
                token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Tokein is missing or invalid'}), 403

        return f(*args, **kwargs)

    return decorated
