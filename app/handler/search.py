#!/usr/bin/env python
# encoding: utf-8

"""
    File name: search.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""
from sqlalchemy import or_

from app import db
from app.models import Application, Tag, Country

def search_application(query_args):
    applications = Application.query
    if 'topic' in query_args:
        applications = applications.filter(or_(
            *[Application.university.ilike("%" + item + "%") for item in query_args['topic']],
            *[Application.major.ilike("%" + item + "%") for item in query_args['topic']],
            *[Application.term.ilike("%" + item + "%") for item in query_args['topic']],
        ))
    if 'university' in query_args:
        applications = applications.filter(Application.university.ilike("%" + query_args['university'] + "%"))
    if 'major' in query_args:
        applications = applications.filter_by(major=query_args['major'])
    if 'result' in query_args:
        applications = applications.filter_by(result=query_args['result'])
    if 'term' in query_args:
        applications = applications.filter(Application.term.ilike("%" + query_args['term'] + "%"))
    if 'degree' in query_args:
        applications = applications.filter_by(degree=query_args['degree'])
    if 'country' in query_args:
        country_id = Country.query.filter_by(name=query_args['country']).first().id;
        applications = applications.filter_by(country_id=country_id)
    if 'tags' in query_args:
        # find the matched applications' id
        tags_set = set()
        for tag in query_args['tags']:
            target_tag = Tag.query.filter(Tag.name.ilike("%"+tag+"%")).first()
            for application in target_tag.applications:
                tags_set.add(application.id)
        applications = applications.filter(Application.id.in_(tags_set))

    # TODO: when nothing matched, should return null.
    return applications.all()