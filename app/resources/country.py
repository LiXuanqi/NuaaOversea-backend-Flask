#!/usr/bin/env python
# encoding: utf-8

"""
    File name:  country.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.handler.country import get_all_countries
from app.utils.fields.country import countries_fields
class Countries(Resource):
    @marshal_with(countries_fields)
    def get(self):
        countries = get_all_countries()
        return {'countries': countries}