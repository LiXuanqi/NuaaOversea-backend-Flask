from app import db
from app.models import User

def register_user(username, password, email):
    user = User(
        username=username,
        password=User.set_password(User, password),
        email=email
    )

    User.add(User, user);

    return {
        'success': 1,
        'user_id': user.id
    }

