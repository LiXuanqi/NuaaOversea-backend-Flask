#!/usr/bin/env python
# encoding: utf-8

"""
    File name: common.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""
from flask_restful import fields

# after post/put with return id
pt_fields = {
    'id': fields.String,
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}

# after delete
deleted_fields = {
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}