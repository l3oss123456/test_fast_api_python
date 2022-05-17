from flask import Blueprint, request, jsonify, session

blueprint = Blueprint('simple_page', __name__, template_folder='templates')
