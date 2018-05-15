import pytest


def test_register(client, app):
    pass

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    pass

def test_login(client, auth):
    pass

# def test_login_validate_input(auth, username, password, message):
#     pass

def test_logout(client, auth):
    pass