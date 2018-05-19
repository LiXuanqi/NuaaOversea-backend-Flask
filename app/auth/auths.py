import datetime, time
import jwt

from app.models import User
from config import Config
class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        Generate Token.
        :param user_id: int
        :param login_time: int(timestamp)
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                Config.TOKEN_SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Verify Token.
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(
                auth_token,
                Config.TOKEN_SECRET_KEY,
                options={
                    'verify_exp': False
                }
            )

            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return "Token 已过期."
        except jwt.InvalidTokenError:
            return '非法的 Token.'

    def authenticate(self, username, password):
        """
        User login, if succeed, write login time into db; Otherwise, return reason of failure.
        :param username:
        :param password:
        :return:
        """

        user_info = User.query.filter_by(username=username).first()
        if (user_info is None):
            return {
                'error': '该用户不存在!'
            }
        else:
            if (User.check_password(User, user_info.password, password)):
                login_time = int(time.time())
                user_info.login_time = login_time
                User.update(User)
                token = self.encode_auth_token(user_info.id, login_time)
                return {
                    'token': token.decode()
                }
            else:
                return {
                    'error': '密码错误!'
                }

    def identify(self, auth_token):
        payload = self.decode_auth_token(auth_token)
        if not isinstance(payload, str):
            user = User.get(User, payload['data']['id'])
            if (user is None):
                result = {
                    'error': '用户不存在'
                }
            else:
                if (user.login_time == payload['data']['login_time']):
                    result = {
                        'user_id': user.id
                    }
                else:
                    result = {
                        'error': 'token 已过期'
                    }
        else:
            result = {
                'error': payload
            }
        return result