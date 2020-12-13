import json
from app import db, create_app
from app.models import Question

def load_db(json_file):

    with open(json_file) as loader:
        json_data = json.load(loader)

    questions = json_data["questions"]
    for question in questions:
        options = question.pop("options")
        for option in options:
            question.update(option)
            q = Question(**question)
            db.session.add(q)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    with app.app_context():
        db.create_all(app=app)
    load_db("questions.json")