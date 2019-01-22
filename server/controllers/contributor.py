from flask import Blueprint, jsonify, request, make_response

from server.helper.sign_up import email_exists, username_exists

bp = Blueprint('contributor', __name__, url_prefix='/api/contributor')

ALREADY_REGISTERED_ERR = '{} already registered in database'


@bp.route('/check_duplicate_username', methods=['POST'])
def check_duplicate_username():
    """Checks if username already exists."""
    username = request.form.get('username')
    if username:
        if username_exists(username):
            res = make_response(
                jsonify({'error': ALREADY_REGISTERED_ERR.format('username')})
                )
            return res, 400
        return make_response(jsonify({'success': 'available username'})), 200
    return make_response(jsonify({'error': 'username not informed'})), 400


@bp.route('/check_duplicate_email', methods=['POST'])
def check_duplicate_email():
    """Checks if email already exists."""
    email = request.form.get('email')
    if email:
        if email_exists(email):
            res = make_response(
                jsonify({'error': ALREADY_REGISTERED_ERR.format('email')})
                )
            return res, 400
        return make_response(jsonify({'success': 'available email'})), 200
    return make_response(jsonify({'error': 'email not informed'})), 400
