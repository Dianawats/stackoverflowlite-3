import logging
from app.api.models.questions import Question
from app.api.db_manager.db_config import DatabaseConnection
from flask import jsonify, make_response

class Answer(Question, DatabaseConnection):
    def __init__(self, user_id, qtn_id, answer_desc, approve):
        DatabaseConnection.__init__(self)
        self.answer_desc = answer_desc
        self.qtn_id = qtn_id
        self.user_id = user_id
        self.approve = approve

    def create_answers_table(self):
        sql = "CREATE TABLE IF NOT EXISTs answers(answer_id SERIAL PRIMARY KEY, qtn_id INT NOT NULL, user_id INT NOT NULL, answer_desc VARCHAR(100) NOT NULL, approve VARCHAR(100)NOT NULL)"
        self.cursor.execute(sql)

    def post_answer(self):
        sql = "INSERT INTO answers(qtn_id, user_id, answer_desc, approve) VALUES(%s, %s, %s, %s) RETURNING qtn_id"
        try:
            with DatabaseConnection() as cursor:
                cursor.execute(sql, (self.qtn_id, self.user_id, self.answer_desc, self.approve))
                cursor.execute("SELECT * FROM answers WHERE qtn_id = '%s'" % self.qtn_id)
                result = cursor.fetchone()
                return jsonify(self.answer_dict(result))
        except Exception as e:
            raise e


    @staticmethod
    def answer_dict(answer):
        return{
            "answer_id": answer[0],
            "qtn_id": answer[1],
            "user_id":answer[2],
            "answer_desc": answer[3],
        }
    
    @staticmethod
    def check_approve_status(answer_id):
        """check the status of the answer whether approved or not"""
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT approve FROM answers WHERE answer_id = '%s'", [answer_id])
            approve = cursor.fetchone()
            if approve =="Yeah":
                return "Best answer"
   
    @staticmethod
    def delete_answer(answer_id, qtn_id):
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM answers WHERE answer_id = '%s'" % answer_id)
            if not cursor.fetchone():
                return {"message": "The answer you are trying to delete doesn't exist"}
            cursor.execute("DELETE FROM answers where answer_id = %s AND user_id = %s", [answer_id, qtn_id])
            return {"message": "DELETE"}

    