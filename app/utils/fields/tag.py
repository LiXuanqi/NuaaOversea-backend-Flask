#!/usr/bin/env python
# encoding: utf-8

"""
    File name: tag.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

# for get /applicant


tag_single_fields = {
    'id': fields.Integer,
    'name': fields.String
}

tags_fields = {
    'tags': fields.List(fields.Nested(tag_single_fields))
}
