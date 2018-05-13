#!/usr/bin/env python
# encoding: utf-8

"""
    File name: user.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""
from flask_restful import Resource
from app.models import User
from app.handler.user import register_user
from app.utils.parsers.user import user_post_parser, user_get_parser
from app.auth.auths import Auth
class Users(Resource):
    def post(self):
        """
        User register
        :return:
        """
        args = user_post_parser.parse_args()
        res = register_user(args['username'], args['password'], args['email']);
        return res

    def get(self):
        """
        GET user info
        :return:
        """
        args = user_get_parser.parse_args()
        result = Auth.identify(Auth, args['token'])
        if (result['status'] and result['user_id']):
            user = User.get(User, result['user_id'])
            result = {
                'status': True,
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'login_time': user.login_time
                },
                'msg': 'succeed'
            }
        return result
