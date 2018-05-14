#!/usr/bin/env python
# encoding: utf-8

"""
    File name: applicant.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import fields

# for get /applicant


applicant_single_fields = {
    'id': fields.Integer,
    'college': fields.String,
    'language_type': fields.String,
    'language_reading': fields.Integer,
    'language_listening': fields.Integer,
    'language_speaking': fields.Integer,
    'language_writing': fields.Integer,
    'gre_verbal': fields.Integer,
    'gre_quantitative': fields.Integer,
    'gre_writing': fields.Integer,
    'research': fields.String,
    'project': fields.String,
    'recommendation': fields.String,
    'email': fields.String,
}

applicants_fields = {
    'applicants': fields.List(fields.Nested(applicant_single_fields))
}

# TODO: repeat with #18 'applicant_single_fields'
# for get /applicant/<application_id>
applicant_detail_fields = {
    'id': fields.Integer,
    'college': fields.String,
    'major': fields.String,
    'gpa': fields.Float,
    'language_type': fields.String,
    'language_reading': fields.Integer,
    'language_listening': fields.Integer,
    'language_speaking': fields.Integer,
    'language_writing': fields.Integer,
    'gre_verbal': fields.Integer,
    'gre_quantitative': fields.Integer,
    'gre_writing': fields.Integer,
    'research': fields.String,
    'project': fields.String,
    'recommendation': fields.String,
    'email': fields.String,
}