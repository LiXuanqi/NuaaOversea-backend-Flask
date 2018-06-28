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
from app.utils.auths import identify

from app.utils.parsers.user import user_post_parser, user_get_parser


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

    def get(self):
        """
        GET user info
        :return:
        """

        args = user_get_parser.parse_args()
        result = identify(args['token'])
        if (result['user_id']):
            user = User.get(User, result['user_id'])
            result = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time,
                'applicant_id': user.applicant_id
            }
            return result
        if (result['error']):
            result = {
                'error': result['error']
            }
            return result
        # abort(410, msg="找不到数据", data=None, status=0)
