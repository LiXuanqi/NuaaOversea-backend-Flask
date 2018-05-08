#!/usr/bin/env python
# encoding: utf-8

"""
    File name: search.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import reqparse

# application search
application_search_get_parser = reqparse.RequestParser()

application_search_get_parser.add_argument(
    'q',
    dest='q',
    required=True,
)
