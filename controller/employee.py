from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from database import db
from utils.middleware.jwtMiddleware import token_requierd
from domains.employees.query import employee_query
from domains.employees.insert import employee_insert
from domains.employees.update import employee_update
from domains.employees.delete import employee_delete


employee_blueprint = Blueprint(
    'employee_blueprint_blueprint', __name__, template_folder='templates')


@employee_blueprint.route("/")
@token_requierd
def get_employees():
    _results = employee_query()
    return jsonify(_results)


@employee_blueprint.route("/<id>")
@token_requierd
def find_employees(id=""):
    _results = employee_query(id)
    return jsonify(_results)


@employee_blueprint.route('/insert')
@token_requierd
def insert_employees():
    result = employee_insert(request.args)
    return result


@employee_blueprint.route('/update')
@token_requierd
def update_employee():
    result = employee_update(request.args)
    return result


@employee_blueprint.route('/delete')
@token_requierd
def delete_employee():
    result = employee_delete(request.args)
    return result
