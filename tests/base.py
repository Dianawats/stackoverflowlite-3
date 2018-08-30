import psycopg2
import unittest
import json
from app import app, app_config
from app.api.models.user import User
from app.api.db_manager.db_config import DatabaseConnection


class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        with DatabaseConnection() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTs users( user_id SERIAL PRIMARY KEY, username VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(12) NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTs answers(answer_id_id SERIAL PRIMARY KEY, qtn_id INT NOT NULL, user_id INT NOT NULL, answer_desc VARCHAR(100) NOT NULL, approve VARCHAR(100) NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTs questions(qtn_id SERIAL PRIMARY KEY, user_id INTEGER NOT NULL, title VARCHAR(100) NOT NULL UNIQUE, subject VARCHAR(200) NOT NULL, qtn_desc VARCHAR(100) NOT NULL)")
    
    def tearDown(self):
        """
        Method to drop tables after the test is run
        """
        with DatabaseConnection() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users CASCADE")
            cursor.execute("DROP TABLE IF EXISTS questions CASCADE")
            cursor.execute("DROP TABLE IF EXISTS answers CASCADE")

    def register_user(self, username, email, password):
        """
        Method for registering a user
        """
        return self.client.post(
            'api/v1/users/signup',
            data=json.dumps(dict(
                username=username,
                email=email,
                password=password
            )
            ),
            content_type='application/json'
        )

    def post_question(self, token, user_id, title, subject, qtn_desc):
        """
        Method for posting a question
        """
        return self.client.post(
            'api/v1/questions',
            data=json.dumps(dict(
                user_id=1,
                title=title,
                subject=subject,
                qtn_desc=qtn_desc
            )
            ),
            content_type='application/json',
            headers=({"token": token})
        )
    
    def update_question(self, token, user_id, qtn_id, title, subject, qtn_desc):
        """
        Method for updating a question
        """
        return self.client.put(
            'api/v1/questions/1',
            data=json.dumps(dict(
                qtn_id=1,
                user_id=1,
                title=title,
                subject=subject,
                qtn_desc=qtn_desc
            )
            ),
            content_type='application/json',
            headers=({"token": token})
        )
    
    def delete_question(self, token, user_id, qtn_id):
        """
        Method for deleting a question
        """
        return self.client.delete('api/v1/question/1', headers=({"token": token}))


    def login_user(self, email, password):
        """
        Method for logging a user with dummy data
        """
        return self.client.post(
            'api/v1/users/login',
            data=json.dumps({
                "email": email,
                "password": password}
            ),
            content_type='application/json'
        )
    
    def get_token(self):
        """Returns user token"""
        self.register_user("dian", "dian@gmail.com", "Cohort11")
        response = self.login_user("dian@gmail.com", "Cohort11")
        data = json.loads(response.data.decode())
        return data['token']
    
    def get_all_questions(self, token):
        """
            Method for retrieving all questions
        """
        return self.client.get('api/v1/questions', headers=({"token": token}))
    
    def get_one_question(self, token):
        """
            Method for retrieving one question from the list
        """
        return self.client.get('api/v1/question/1', headers=({"token": token}))
    
    def delete_all_questions(self, token):
        """
            Method for deleting all questions
        """
        return self.client.delete('api/v1/questions', headers=({"token": token}))

    
    def post_answer(self, token, user_id, qtn_id, answer_desc):
        """
            Method for posting an answer for a question
        """
        return self.client.post(
            'api/v1/answer/1',
            data=json.dumps(dict(
                answer_desc = answer_desc,
                qtn_id = qtn_id,
                user_id = user_id

            )
            ),
            content_type='application/json',
            headers=({"token": token})
        )
    
    def delete_answer(self, token, user_id, qtn_id, answer_id):
        """Method for delete answer"""
        return self.client.delete('api/v1/answer/1/1', headers=({"token": token}))

    def delete_all_answers(self, token, user_id, qtn_id):
        """Method to delete all answers"""
        return self.client.delete('api/v1/answers/1', headers=({"token": token}))
    
    def get_all_answers(self, token, qtn_id):
        """Method to retrieve all answers"""
        return self.client.get('api/v1/answer/1', headers=({"token": token}))
    
    def get_one_answer(self, token, qtn_id, answer_id):
        """Method for retrieving one answer"""
        return self.client.get('api/v1/answer/1/1', headers=({"token": token}))

    def delete_question_with_no_token(self, token, user_id, qtn_id):
        """
        Method for deleting a question
        """
        return self.client.delete('api/v1/question/1')
