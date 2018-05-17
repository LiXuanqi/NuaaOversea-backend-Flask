
from app.models import User

def register_user(username, password, email, will_contact):
    user = User(
        username=username,
        password=User.set_password(User, password),
        email=email,
        will_contact=will_contact
    )

    User.add(User, user);

    return {
        'id': user.id
    }

