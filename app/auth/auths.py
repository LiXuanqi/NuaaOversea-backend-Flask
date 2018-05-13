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
            return "Token is expired."
        except jwt.InvalidTokenError:
            return 'Invalid token.'

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
                'status': False,
                'msg': 'user is not existed.'
            }
        else:
            if (User.check_password(User, user_info.password, password)):
                login_time = int(time.time())
                user_info.login_time = login_time
                User.update(User)
                token = self.encode_auth_token(user_info.id, login_time)
                return {
                    'status': True,
                    'data': {
                        'token': token.decode()
                    },
                    'msg': 'Login succeed'
                }
            else:
                return {
                    'status': False,
                    'msg': 'wrong password'
                }

    def identify(self, auth_token):
        payload = self.decode_auth_token(auth_token)
        if not isinstance(payload, str):
            user = User.get(User, payload['data']['id'])
            if (user is None):
                result = {
                    'status': False,
                    'msg': 'user does not exist'
                }
            else:
                if (user.login_time == payload['data']['login_time']):
                    result = {
                        'status': True,
                        'msg': 'succeed',
                        'user_id': user.id
                    }
                else:
                    result = {
                        'status': False,
                        'msg': 'token is expired'
                    }
        else:
            result = {
                'status': False,
                'msg': payload
            }
        return result