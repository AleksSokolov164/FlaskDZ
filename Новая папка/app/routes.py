from flask import Blueprint
from .models import db
from .models import User

user = Blueprint('user', __name__)

@user.route('/user/<login>')
def create_user(login):
    user = User(login=login)
    db.session.add(user)
    db.session.commit()
    return 'Ok'
