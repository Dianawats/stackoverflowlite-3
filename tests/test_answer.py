import json

from tests.base import BaseTestCase
from app.api.models.answer import Answer


class TestAnswers(BaseTestCase):

    """Class for testing user annswers"""
    
    def test_if_json_data(self):
        """
            Test for json data
        """
        with self.client:
            token = self.get_token()
            response = self.post_answer(token, 1, 1, "Use static methods")
            self.assertTrue(response.content_type == 'application/json')
            
    def test_answer_class(self):
        """Test for existence of answer model"""
        answer = Answer(1, 1, 'python oop', 'yes')
        self.assertTrue(answer)
    
    def test_json_data_error_response(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            token = self.get_token()
            response = self.post_answer(token, 1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")
    
    def test_json_data_error_response_code(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            token = self.get_token()
            response = self.post_answer(token, 1, 1, "Use static methods")
            self.assertNotEqual(response.status_code, 400)

    def test_successful_answering(self):
        """
            Test for successful posting of 
            user answers for a specific question
        """
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            response = self.post_answer(token, 1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['answer'])

    def test_answering_to_non_existing_question(self):
        """Test for trying to answering 
            to a question that doesn't exist
        """
        with self.client:
            token = self.get_token()
            response = self.post_answer(token, 1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get("message"), "Question not found")
    
    def test_delete_answer(self):
        """Test  if an answer can be deleted"""
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "control version")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.delete_answer(token, 1, 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['Answers left'], [])

    def test_unauthorized_delete_of_a_answer(self):
        """Test if a non-registered user can delete an answer"""
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "control version")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.delete_answer('token', 1, 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'], 'Invalid token. Please log in again.')
        
    def test_delete_answers(self):
        """Test  if all answers can be deleted at once"""
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.delete_all_answers(token, 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['Answers left'], [])

    def test_unauthorized_delete_of_all_answers(self):
        """Test if an unauthorized user can delete an answer"""
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.delete_all_answers('token', 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'Invalid token. Please log in again.')
    
    def test_get_all_answers_status_code(self):
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.get_all_answers(token, 1)
            self.assertEqual(response.status_code, 200)

    def test_get_all_answers(self):
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.get_all_answers(token, 1)
            data = json.loads(response.data.decode())
            self.assertTrue(data['answers'])

    def test_get_one_answer(self):
        with self.client:
            token = self.get_token()
            self.post_question(token, 1, "git", "github", "version control")
            self.post_answer(token, 1, 1, "Use static methods")
            response = self.get_one_answer(token, 1, 1)
            data = json.loads(response.data.decode())
            self.assertTrue(data['answer'])
