#!/usr/bin/env python
# encoding: utf-8

"""
    File name: auto_tags.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Tag
def auto_tags(gre, gpa, is_transfer, toefl=None, ielts=None):
    tags = []
    # TODO: the standar of IELTS.
    # TOEFL
    if toefl is not None:
        if toefl >= 105 and gre >= 325:
            tags.append(Tag.query.filter_by(name="高GT").first())
        if gpa <= 3 and toefl <= 95 and gre <= 315:
            tags.append(Tag.query.filter_by(name="低三维").first())
    # IELTS
    if ielts is not None:
        if ielts >= 8 and gre >= 325:
            tags.append(Tag.query.filter_by(name="高GT").first())
        if gpa <= 3 and ielts <= 6 and gre <= 315:
            tags.append(Tag.query.filter_by(name="低三维").first())

    if is_transfer == True:
        tags.append(Tag.query.filter_by(name="转专业").first())
    if gpa >= 3.9 :
        tags.append(Tag.query.filter_by(name="高GPA").first())
    return tags