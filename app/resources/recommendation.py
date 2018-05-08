#!/usr/bin/env python
# encoding: utf-8

"""
    File name:  recommendation.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.handler.recommendation import get_all_recommendations
from app.utils.fields.recommendation import recommendations_fields

class Recommendations(Resource):
    @marshal_with(recommendations_fields)
    def get(self):
        recommendations = get_all_recommendations()
        return {'recommendations': recommendations}