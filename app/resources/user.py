#!/usr/bin/env python
# encoding: utf-8

"""
    File name: user.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""
from flask_restful import Resource

from app.handler.user import register_user
from app.models import User
from app.utils.auths import login_required, decode_user_id

from app.utils.parsers.user import user_post_parser


class Users(Resource):
    def post(self):
        """
        User register
        :return:
        """
        # TODO: while the user that wanted to be register is existed, should throw error.
        args = user_post_parser.parse_args()
        res = register_user(args['username'], args['password'], args['email'], args['will_contact']);
        return res

    @login_required
    def get(self):
        """
        GET user info
        :return:
        """
        user_id = decode_user_id()
        user = User.get(User, user_id)
        result = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time,
            'applicant_id': user.applicant_id
        }
        return result
