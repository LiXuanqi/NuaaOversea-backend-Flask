#!/usr/bin/env python
# encoding: utf-8

"""
    File name: research.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Research

def get_all_researches():
    researches = Research.query.all()
    return researches