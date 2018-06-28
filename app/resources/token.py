#!/usr/bin/env python
# encoding: utf-8

"""
    File name: token.py
    Function Des:


    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource

from app.utils.auths import authenticate
from app.utils.parsers.token import login_post_parser


class Tokens(Resource):
    def post(self):
        """
        User login.
        :return:
        """
        args = login_post_parser.parse_args()

        return authenticate(args['username'], args['password'])