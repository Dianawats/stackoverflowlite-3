import logging

from flask import Blueprint, request, jsonify, make_response
from app.api.models.questions import Question
from app.api.models.user import User
from app.api.models.answer import Answer
from app.api.views.decorators import login_required

answers = Blueprint('answers', __name__)


@answers.route('/api/v1/question/<int:qtn_id>/answer', methods=['POST'])
@login_required
def post_answer(user_id, qtn_id):
    try:
        if not request.get_json():
            return make_response(jsonify({"message": "Request should be json"}), 400)
        qtn_id = request.get_json()['qtn_id']
        user_id = request.get_json()['user_id']
        approve = request.get_json()['approve']
        answer_desc = request.get_json()['answer_desc']
        answer_instance = Answer(user_id, qtn_id, answer_desc, approve)
        print(answer_instance)

        answer = Answer.post_answer(answer_instance)
        print(answer)
        return answer
       
    except Exception as e:
        raise e
        # logging.error(e)
        # return make_response(jsonify({'message': str(e)}), 500)
