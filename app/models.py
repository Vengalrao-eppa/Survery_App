from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    response = db.relationship('UsersResponse', backref='response', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qid = db.Column(db.Integer, nullable=False)
    qtext = db.Column(db.String(200), nullable=False)
    qtype = db.Column(db.String(20), nullable=False)
    options = db.Column(db.String(200), nullable=True)
    next_question = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<QuestionID: {self.id}>'


class UsersResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_response = db.Column(db.String(200))