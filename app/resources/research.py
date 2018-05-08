#!/usr/bin/env python
# encoding: utf-8

"""
    File name:  research.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.handler.research import get_all_researches
from app.utils.fields.research import researches_fields

class Researches(Resource):
    @marshal_with(researches_fields)
    def get(self):
        researches = get_all_researches()
        return {'researches': researches}