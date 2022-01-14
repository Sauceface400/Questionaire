from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

class Questions:
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)

    def __init__(self, answer):
        self.answer = answer
