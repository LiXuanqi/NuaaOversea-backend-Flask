#!/usr/bin/env python
# encoding: utf-8

"""
    File name: application.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

# for get /applications
tag_single_fileds = {
    'id': fields.String,
    'name': fields.String
}
project_single_fileds = {
    'id': fields.String,
    'name': fields.String,
    'value': fields.Integer
}
research_single_fileds = {
    'id': fields.String,
    'name': fields.String,
    'value': fields.Integer
}
recommendation_single_fileds = {
    'id': fields.String,
    'name': fields.String,
    'value': fields.Integer
}
# TODO: complete the response format for 'get /applications'.
application_single_fields = {
    'id': fields.String,
    'country': fields.String(attribute='country.name'),
    'university': fields.String,
    'major': fields.String,
    'term': fields.String,
    'degree': fields.String,
    'result': fields.String,
    'applicant_id': fields.Integer,
    'gpa': fields.Float(attribute='applicant.gpa'),
    'language_type': fields.String(attribute='applicant.language_type'),
    'language_reading': fields.Integer(attribute='applicant.language_reading'),
    'language_listening': fields.Integer(attribute='applicant.language_listening'),
    'language_speaking': fields.Integer(attribute='applicant.language_speaking'),
    'language_writing': fields.Integer(attribute='applicant.language_writing'),
    'gre_verbal': fields.Integer(attribute='applicant.gre_verbal'),
    'gre_quantitative': fields.Integer(attribute='applicant.gre_quantitative'),
    'gre_writing': fields.Float(attribute='applicant.gre_writing'),
    'tags': fields.List(fields.Nested(tag_single_fileds))
}

applications_fields = {
    'applications': fields.List(fields.Nested(application_single_fields))
}

# TODO: repeat with #18 'application_single_fields'
# for get /application/<application_id>
application_detail_fields = {
    'id': fields.String,
    'country': fields.String(attribute='country.name'),
    'university': fields.String,
    'major': fields.String,
    'term': fields.String,
    'degree': fields.String,
    'result': fields.String,
    'applicant_id': fields.Integer,
    'gpa': fields.Float(attribute='applicant.gpa'),
    'language_type': fields.String(attribute='applicant.language_type'),
    'language_reading': fields.Integer(attribute='applicant.language_reading'),
    'language_listening': fields.Integer(attribute='applicant.language_listening'),
    'language_speaking': fields.Integer(attribute='applicant.language_speaking'),
    'language_writing': fields.Integer(attribute='applicant.language_writing'),
    'gre_verbal': fields.Integer(attribute='applicant.gre_verbal'),
    'gre_quantitative': fields.Integer(attribute='applicant.gre_quantitative'),
    'gre_writing': fields.Float(attribute='applicant.gre_writing'),
    'tags': fields.List(fields.Nested(tag_single_fileds)),
    'project': fields.Nested(project_single_fileds, attribute='applicant.project'),
    'recommendation': fields.Nested(recommendation_single_fileds, attribute='applicant.recommendation'),
    'research': fields.Nested(research_single_fileds, attribute='applicant.research'),
}