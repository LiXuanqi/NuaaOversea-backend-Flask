#!/usr/bin/env python
# encoding: utf-8

"""
    File name: country.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

# for get /applicant


country_single_fields = {
    'id': fields.Integer,
    'name': fields.String
}

countries_fields = {
    'countries': fields.List(fields.Nested(country_single_fields))
}
