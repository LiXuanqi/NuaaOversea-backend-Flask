#!/usr/bin/env python
# encoding: utf-8

"""
    File name: token.py
    Function Des:


    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from flask_restful import Resource, marshal_with
from app.utils.parsers.token import login_post_parser
from app import redis_store
import requests
from app.models import User
from app import db
from app.utils.fields.user import user_single_fields
class Tokens(Resource):
    def post(self):
        """POST /token?code=xxx&redirect_uri=xxx

        Get token from /sso-v2 and store it into redis.

        :arg:
            code: get from sso-v2
            redirect_uri: link to redirect

        :return:
            For example:
            {"access_token": xxx}

        """
        # TODO: while redirect_uri and code are missing, return error message.
        args = login_post_parser.parse_args()
        code = args['code']
        redirect_uri = args['redirect_uri']

        if code is None or redirect_uri is None:
            return {
                'message': 'params missing'
            }

        token_response = requests.post('http://127.0.0.1/sso-v2/api/', data={
            'service': 'App.Oauth.GetAccessToken',
            'appid': '12345678',
            'appsecret': '12345678',
            'code': code
        })
        response_data = token_response.json()['data']
        access_token = response_data['access_token']
        expires_in = response_data['expires_in']

        # get user_id by access_token
        user_response = requests.post('http://127.0.0.1/sso-v2/api/', data={
            'service': 'App.Oauth.GetUserInfo',
            'access_token': access_token,
            'types': 'id,name,username,stu_num'
        })
        response_data = user_response.json()['data']
        user_id = response_data['id']
        name = response_data['name']
        username = response_data['username']
        stu_num = response_data['stu_num']

        user = User.query.filter_by(id=user_id).first()
        if user is None:
            new_user = User(
                id=user_id,
                username=username,
                name=name,
                stu_num=stu_num,
                role='student',
            )
            db.session.add(new_user)
            db.session.commit()

        redis_store.set(access_token, user_id)
        redis_store.expire(access_token, expires_in)

        return {
            'access_token': access_token,
            'redirect_uri': redirect_uri
        }


class Token(Resource):
    @marshal_with(user_single_fields)
    def get(self, access_token):
        """GET /token/xxx
        :arg:
            access_token
        :return:
            user information and login status.
        """
        user_id = redis_store.get(access_token)
        if user_id is None:
            return {
                'message': 'access_token is invalid'
            }
        user = User.query.filter_by(id=user_id).first()
        return user

    def delete(self, access_token):
        """DELETE /token/xxx

        :return:
        """
        if not redis_store.exists(access_token):
            return {
                'message': 'access_token does not exist.'
            }

        redis_store.delete(access_token)
        return {
            'message': access_token + ' is deleted'
        }