from flask import Blueprint, jsonify, request, make_response

from server.helpers.sign_up import (email_exists,
                                    username_exists,
                                    register_user,
                                    get_missing_fields,)


bp = Blueprint('sign_up', __name__, url_prefix='/api/sign_up')

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
            return res, 409
        return make_response(jsonify({'success': 'available username'})), 200
    return make_response(jsonify({'error': 'username not informed'})), 422


@bp.route('/check_duplicate_email', methods=['POST'])
def check_duplicate_email():
    """Checks if email already exists."""
    email = request.form.get('email')
    if email:
        if email_exists(email):
            res = make_response(
                jsonify({'error': ALREADY_REGISTERED_ERR.format('email')})
            )
            return res, 409
        return make_response(jsonify({'success': 'available email'})), 200
    return make_response(jsonify({'error': 'email not informed'})), 422


@bp.route('register_user', methods=['POST'])
def register_new_user():
    missing_fields = get_missing_fields(request.form)
    if missing_fields:
        res = make_response(
            jsonify({'missing_parameters': missing_fields})
        )
        return res, 422

    if email_exists(request.form['email']):
        res = make_response(
            jsonify({'error': ALREADY_REGISTERED_ERR.format('email')})
        )
        return res, 409

    if username_exists(request.form['username']):
        res = make_response(
                jsonify({'error': ALREADY_REGISTERED_ERR.format('username')})
            )
        return res, 409

    register_user(request.form)
    return make_response(
        jsonify({'success': 'user registered'})
    )
