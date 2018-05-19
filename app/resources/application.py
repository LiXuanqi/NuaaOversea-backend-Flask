#!/usr/bin/env python
# encoding: utf-8

"""
    File name: application.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with, abort

from app.auth.auths import Auth
from app.handler.application import get_all_applications, create_application, get_applications_by_applicantid, get_applications_by_university
from app.handler.application import get_application_by_id, update_application, rm_application

from app.utils.fields.common import pt_fields, deleted_fields
from app.utils.fields.application import applications_fields, application_detail_fields

from app.utils.parsers.application import application_post_parser, application_put_parser, applications_get_parser, \
    application_delete_parser


class Applications(Resource):
    @marshal_with(applications_fields)
    def get(self):
        applications_args = applications_get_parser.parse_args()

        if(applications_args['applicant_id']):
            applicant_id = applications_args['applicant_id']
            applications = get_applications_by_applicantid(applicant_id)
            return {'applications': applications}

        if(applications_args['university']):
            university = applications_args['university']
            applications = get_applications_by_university(university)
            return {'applications': applications}

        applications = get_all_applications()
        return {'applications': applications}

    def post(self):
        application_args = application_post_parser.parse_args()
        result = Auth.identify(Auth, application_args['token'])
        if ('error' in result.keys()):
            result = {
                'error': result['error']
            }
            return result
        if ('user_id' in result.keys()):

            result = create_application(
                application_args.country_id,
                application_args.university,
                application_args.major,
                application_args.degree,
                application_args.term,
                application_args.result,
                application_args.applicant_id,
                application_args.is_transfer
            )
            return result

class Application(Resource):
    @marshal_with(application_detail_fields)
    def get(self, application_id):
        application = get_application_by_id(application_id)
        return application

    def put(self, application_id):
        application_args = application_put_parser.parse_args()

        result = Auth.identify(Auth, application_args['token'])
        if ('error' in result.keys()):
            result = {
                'error': result['error']
            }
            return result
        if ('user_id' in result.keys()):

            result = update_application(
                application_id,
                application_args.country_id,
                application_args.university,
                application_args.major,
                application_args.degree,
                application_args.term,
                application_args.result,
                application_args.applicant_id,
                application_args.is_transfer
            )
            return result

    def delete(self, application_id):

        application_args = application_delete_parser.parse_args()

        result = Auth.identify(Auth, application_args['token'])
        if ('error' in result.keys()):
            result = {
                'error': result['error']
            }
            return result
        if ('user_id' in result.keys()):

            result = rm_application(application_id)
            if result is True:
                return ''

