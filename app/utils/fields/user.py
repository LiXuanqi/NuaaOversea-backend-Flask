#!/usr/bin/env python
# encoding: utf-8

"""
    File name: user.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

user_single_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'stu_num': fields.String,
    'role': fields.String,
    'applicant_id': fields.Integer
}
