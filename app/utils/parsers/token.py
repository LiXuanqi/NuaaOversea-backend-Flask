#!/usr/bin/env python
# encoding: utf-8

"""
    File name: token.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import reqparse

# post
login_post_parser = reqparse.RequestParser()

login_post_parser.add_argument(
    'username',
    dest='username',
    required=True,
)

login_post_parser.add_argument(
    'password',
    dest='password',
    required=True,
)