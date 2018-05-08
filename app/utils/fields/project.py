#!/usr/bin/env python
# encoding: utf-8

"""
    File name: project.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

project_single_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'value': fields.Integer
}

projects_fields = {
    'projects': fields.List(fields.Nested(project_single_fields))
}
