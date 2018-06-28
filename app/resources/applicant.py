#!/usr/bin/env python
# encoding: utf-8

"""
    File name: applicant.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""


from flask_restful import Resource, marshal_with, marshal

from app.handler.applicant import get_all_applicants, create_applicant, patch_applicant
from app.handler.applicant import get_applicant_by_id, update_applicant, rm_applicant
from app.utils.auths import login_required, decode_user_id
from app.utils.fields.applicant import applicants_fields, applicant_detail_fields
from app.utils.fields.common import deleted_fields
from app.utils.parsers.applicant import applicant_post_parser, applicant_put_parser, applicant_patch_parser, \
    applicant_delete_parser


class Applicants(Resource):
    @marshal_with(applicants_fields)
    def get(self):
        applicants = get_all_applicants()
        return {'applicants': applicants}
    @login_required
    def post(self):
        applicant_args = applicant_post_parser.parse_args()
        user_id = decode_user_id()
        result = create_applicant(
            user_id,
            applicant_args.college,
            applicant_args.major,
            applicant_args.gpa,
            applicant_args.language_type,
            applicant_args.language_reading,
            applicant_args.language_listening,
            applicant_args.language_speaking,
            applicant_args.language_writing,
            applicant_args.gre_verbal,
            applicant_args.gre_quantitative,
            applicant_args.gre_writing,
            applicant_args.research_id,
            applicant_args.project_id,
            applicant_args.recommendation_id
        )
        return result


class Applicant(Resource):
    # @marshal_with(applicant_detail_fields)
    # FIXME: when call the applicant that does not exist, it should return error message.
    def get(self, applicant_id):
        result = get_applicant_by_id(applicant_id)
        if result is None:
            return {}
        else:
            return marshal(result, applicant_detail_fields), 200

    @login_required
    def put(self, applicant_id):

        applicant_args = applicant_put_parser.parse_args()

        result = update_applicant(
            applicant_id,
            applicant_args.college,
            applicant_args.major,
            applicant_args.gpa,
            applicant_args.language_type,
            applicant_args.language_reading,
            applicant_args.language_listening,
            applicant_args.language_speaking,
            applicant_args.language_writing,
            applicant_args.gre_verbal,
            applicant_args.gre_quantitative,
            applicant_args.gre_writing,
            applicant_args.research_id,
            applicant_args.project_id,
            applicant_args.recommendation_id
        )

        return result

    @login_required
    @marshal_with(deleted_fields)
    def delete(self, applicant_id):
        applicant_args = applicant_delete_parser.parse_args()

        result = rm_applicant(applicant_id)
        return result

    @login_required
    @marshal_with(applicant_detail_fields)
    def patch(self, applicant_id):
        args = applicant_patch_parser.parse_args()

        result = patch_applicant(
            applicant_id,
            args.college,
            args.major,
            args.gpa,
            args.language_type,
            args.language_reading,
            args.language_listening,
            args.language_speaking,
            args.language_writing,
            args.gre_verbal,
            args.gre_quantitative,
            args.gre_writing,
            args.research_id,
            args.project_id,
            args.recommendation_id
        )

        return result;