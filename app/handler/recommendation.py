#!/usr/bin/env python
# encoding: utf-8

"""
    File name: recommendation.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Recommendation

def get_all_recommendations():
    recommendations = Recommendation.query.all()
    return recommendations