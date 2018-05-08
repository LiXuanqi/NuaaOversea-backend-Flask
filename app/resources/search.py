#!/usr/bin/env python
# encoding: utf-8

"""
    File name: search.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.utils.parsers.search import application_search_get_parser
from app.utils.query_args_parser import query_args_parser
from app.handler.search import search_application
from app.utils.fields.application import applications_fields

class ApplicationSearch(Resource):
    @marshal_with(applications_fields)
    def get(self):
        args = application_search_get_parser.parse_args()
        query_args = query_args_parser(args['q']);
        # TODO：NAME, YEAR, TAG
        # TODO: filter from mysql by orm.
        applications = search_application(query_args)
        return {'applications': applications}