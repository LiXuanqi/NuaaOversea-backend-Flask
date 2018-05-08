#!/usr/bin/env python
# encoding: utf-8

"""
    File name: tag.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.handler.tag import get_all_tags
from app.utils.fields.tag import tags_fields
class Tags(Resource):
    @marshal_with(tags_fields)
    def get(self):
        tags = get_all_tags()
        return {'tags': tags}