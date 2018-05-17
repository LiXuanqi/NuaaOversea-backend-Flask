#!/usr/bin/env python
# encoding: utf-8

"""
    File name: user.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import reqparse

# get
user_get_parser = reqparse.RequestParser()

user_get_parser.add_argument(
    'token',
    dest='token',
    required=True,
    location='args'
)

# post
user_post_parser = reqparse.RequestParser()

user_post_parser.add_argument(
    'username',
    dest='username',
    required=True,
)

user_post_parser.add_argument(
    'password',
    dest='password',
    required=True,
)

user_post_parser.add_argument(
    'email',
    dest='email',
    required=False,
)
user_post_parser.add_argument(
    'will_contact',
    dest='will_contact',
    required=True,
    type=bool
)