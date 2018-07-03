#!/usr/bin/env python
# encoding: utf-8

"""
    File name: application.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""


from flask_restful import reqparse
# -------- applications get parser --------
applications_get_parser = reqparse.RequestParser()

applications_get_parser.add_argument(
    'applicant_id',
    dest='applicant_id',
    type=str,
    location='args',
    required=False,
)
applications_get_parser.add_argument(
    'university',
    dest='university',
    type=str,
    location='args',
    required=False,
)
# -------- application add parser --------
application_post_parser = reqparse.RequestParser()

application_post_parser.add_argument(
    'token',
    dest='token',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'applicant_id',
    dest='applicant_id',
    type=str,
    required=True,
)


application_post_parser.add_argument(
    'country_id',
    dest='country_id',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'degree',
    dest='degree',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'university',
    dest='university',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'major',
    dest='major',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'term',
    dest='term',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'result',
    dest='result',
    type=str,
    required=True,
)

application_post_parser.add_argument(
    'is_transfer',
    dest='is_transfer',
    type=bool,
    required=True,
)


# -------- application update parser --------
application_put_parser = reqparse.RequestParser()

application_put_parser.add_argument(
    'applicant_id',
    dest='applicant_id',
    type=str,
    required=True,
)


application_put_parser.add_argument(
    'country_id',
    dest='country_id',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'degree',
    dest='degree',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'university',
    dest='university',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'major',
    dest='major',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'term',
    dest='term',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'result',
    dest='result',
    type=str,
    required=True,
)

application_put_parser.add_argument(
    'is_transfer',
    dest='is_transfer',
    type=bool,
    required=True,
)


# -------- application patch parser --------
application_patch_parser = reqparse.RequestParser()

application_patch_parser.add_argument(
    'applicant_id',
    dest='applicant_id',
    type=str,
)

application_patch_parser.add_argument(
    'country_id',
    dest='country_id',
    type=str
)

application_patch_parser.add_argument(
    'degree',
    dest='degree',
    type=str
)

application_patch_parser.add_argument(
    'university',
    dest='university',
    type=str
)

application_patch_parser.add_argument(
    'major',
    dest='major',
    type=str
)

application_patch_parser.add_argument(
    'term',
    dest='term',
    type=str
)

application_patch_parser.add_argument(
    'result',
    dest='result',
    type=str
)

application_patch_parser.add_argument(
    'is_transfer',
    dest='is_transfer',
    type=bool
)

application_delete_parser = reqparse.RequestParser()

application_delete_parser.add_argument(
    'token',
    dest='token',
    type=str,
    location='args',
    required=True,
)
