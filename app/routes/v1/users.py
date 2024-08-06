from flask import Blueprint, jsonify

bp = Blueprint('v1_users', __name__)

@bp.route('/users')
def get_users_v1():
    return jsonify({'message': 'Users from API version 1'})
