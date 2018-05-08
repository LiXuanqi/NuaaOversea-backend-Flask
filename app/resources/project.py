#!/usr/bin/env python
# encoding: utf-8

"""
    File name:  project.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.handler.project import get_all_projects
from app.utils.fields.project import projects_fields

class Projects(Resource):
    @marshal_with(projects_fields)
    def get(self):
        projects = get_all_projects()
        return {'projects': projects}