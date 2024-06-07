from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    pasword = db.Column(db.String(50))
    u_one = db.Column(db.Integer)
    u_two = db.Column(db.Integer)
    u_three = db.Column(db.Integer)
    u_four = db.Column(db.Integer)
    u_five = db.Column(db.Integer)
