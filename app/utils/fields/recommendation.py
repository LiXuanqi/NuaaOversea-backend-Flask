#!/usr/bin/env python
# encoding: utf-8

"""
    File name: recommendation.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

recommendation_single_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'value': fields.Integer
}

recommendations_fields = {
    'recommendations': fields.List(fields.Nested(recommendation_single_fields))
}
