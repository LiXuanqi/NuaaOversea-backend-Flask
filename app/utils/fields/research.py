#!/usr/bin/env python
# encoding: utf-8

"""
    File name: research.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

research_single_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'value': fields.Integer
}

researches_fields = {
    'researches': fields.List(fields.Nested(research_single_fields))
}
