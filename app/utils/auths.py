import datetime, time

import functools
import jwt
from flask import request
from flask_restful import abort

from app.models import User
from config import Config

def encode_auth_token(user_id, login_time):
    """
    Generate Token.
    :param user_id: int
    :param login_time: int(timestamp)
    :return:
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
            'iat': datetime.datetime.utcnow(),
            'iss': 'ken',
            'data': {
                'id': user_id,
                'login_time': login_time
            }
        }
        return jwt.encode(
            payload,
            Config.TOKEN_SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Verify Token.
    :param auth_token:
    :return:
    """
    try:
        payload = jwt.decode(
            auth_token,
            Config.TOKEN_SECRET_KEY,
            options={
                'verify_exp': False
            }
        )

        if ('data' in payload and 'id' in payload['data']):
            return payload
        else:
            raise jwt.InvalidTokenError
    except jwt.ExpiredSignatureError:
        abort(401, error="Token 已过期")
    except jwt.InvalidTokenError:
        abort(401, error="非法的Token")

def authenticate(username, password):
    """
    User login, if succeed, write login time into db; Otherwise, return reason of failure.
    :param username:
    :param password:
    :return:
    """

    user_info = User.query.filter_by(username=username).first()
    if (user_info is None):
        abort(401, error="用户不存在")
    else:
        if (User.check_password(User, user_info.password, password)):
            login_time = int(time.time())
            user_info.login_time = login_time
            User.update(User)
            token = encode_auth_token(user_info.id, login_time)
            return {
                'token': token.decode()
            }
        else:
            abort(401, error="密码错误")

def identify(auth_token):
    payload = decode_auth_token(auth_token)
    if not isinstance(payload, str):
        user = User.get(User, payload['data']['id'])
        if (user is None):
            result = {
                'error': '用户不存在'
            }
        else:
            if (user.login_time == payload['data']['login_time']):
                result = {
                    'user_id': user.id
                }
            else:
                result = {
                    'error': 'token 已过期'
                }
    else:
        result = {
            'error': payload
        }
    return result

def decode_user_id():
    payload = decode_auth_token(request.headers['Token'])
    return payload['data']['id']

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        headers = request.headers
        print(headers)
        if 'Token' not in headers:
            abort(401, error="没有Token.")
        else:
            auth_token = headers['Token']
            payload = decode_auth_token(auth_token)
            if not isinstance(payload, str):
                user = User.get(User, payload['data']['id'])
                if user is None:
                    abort(401, error="用户不存在")
                else:
                    if user.login_time == payload['data']['login_time']:
                        return func(*args, **kw)
                    else:
                        abort(401, error="Token已过期")
            else:
                abort(401, error=payload + " 是非法的.")



    return wrapper