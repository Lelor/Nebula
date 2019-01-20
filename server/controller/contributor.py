from flask import Blueprint, jsonify, request

from server.database.model import User
from server.helper.sign_up import email_exists, username_exists

bp = Blueprint('contributor', __name__, url_prefix='/api/contributor')

ALREADY_REGISTERED_ERR = '{} already registered in database'

@bp.route('check_duplicate', methods=['POST'])
def check_duplicate_username():
    username = request.form['username']
    if username_exists(username):
        return jsonify({'error': ALREADY_REGISTERED_ERR.format('username')})
    return jsonify({'success': 'available username'})
    

@bp.route('check_duplicate', methods=['POST'])
def check_duplicate_email():
    email = request.form['email']
    if email_exists(email):
        return jsonify({'error': ALREADY_REGISTERED_ERR.format('email')})
    return jsonify({'success': 'available email'})
