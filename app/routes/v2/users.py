from flask import Blueprint, jsonify

bp = Blueprint('v2_users', __name__)

@bp.route('/users')
def get_users_v2():
    return jsonify({'message': 'Users from API version 2'})
