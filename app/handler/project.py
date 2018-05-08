#!/usr/bin/env python
# encoding: utf-8

"""
    File name: project.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Project

def get_all_projects():
    projects = Project.query.all()
    return projects