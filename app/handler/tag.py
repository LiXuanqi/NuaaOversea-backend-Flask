#!/usr/bin/env python
# encoding: utf-8

"""
    File name: tag.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Tag

def get_all_tags():
    tags = Tag.query.all()
    return tags