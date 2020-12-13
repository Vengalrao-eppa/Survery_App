import os
from flask import Blueprint, jsonify, request, url_for
from app import db
from app.models import User, Question, UsersResponse


main = Blueprint('main', __name__)
base_url = "/api/v1"

# load questions table
def load_questions():
    qdict = {}
    questions = Question.query.all()
    for question in questions:
        qdict[question.id] = {
            "qno": question.qid,
            "qtype": question.qtype,
            "qtext": question.qtext,
            "qans": question.options,
            "qnext": question.next_question
        }
    return qdict


@main.route(f"{base_url}/home", methods=["GET", "POST"])
def home():

    status_code = 200
    response = {
        "message": "welcome to the Survey App!"
        }

    if request.method == "POST":
        if not request.json or not "email" in request.json or not "name" in request.json:
            response["payload"] = "email/name is required.."
            status_code = 400
        else:
            payload = request.json
            username = payload["name"]
            email = payload["email"]
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()

            response["message"] = "User Created successfully.."
            response["next_url"] = request.host + url_for("main.questions")
            
    return jsonify(response), status_code


@main.route(f"{base_url}/questions", methods=["GET"])
def questions():    
    questions = load_questions()
    return jsonify({"questions": str(questions)})
    #next_url = request.base_url + f"?question={qid}"


@main.route(f"{base_url}/question/<qid>", methods=["POST"])
def qpost(qid):
    question = Question.query.filter_by(id=qid).first()
    if not question:
        return jsonify({"payload": "question details not found.."})
    return jsonify({
        "payload": {
            "qno": question.qid,
            "qtype": question.qtype,
            "qtext": question.qtext,
            "qans": question.options,
            "qnext": question.next_question
        }
    })


@main.route(f"{base_url}/<user_id>", methods=["POST"])
def qsave(user_id):

    # payload should be a list of captured user responses of all questions
    responses = request.json
    for response in responses:
        ur = UsersResponse(**response)
        db.session.add(ur)
    db.session.commit()

    return jsonify({"message": "success"})