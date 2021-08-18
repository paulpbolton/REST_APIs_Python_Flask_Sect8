import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # nb to note that the db column names need to match the object properties below

    def __init__(self, username, password):
        # note ID has been removed as it auto increments
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # Returns SELECT * FROM users

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
