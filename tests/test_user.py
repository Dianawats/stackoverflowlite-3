import json
from tests.base import BaseTestCase
from app.api.models.user import User

class TestUserAuth(BaseTestCase):


    def test_if_user_class_exists(self):
        user = User(1,"dian", "dian@gmail.com", "Cohort11")
        self.assertTrue(user)

    def test_if_json_data(self):
        """
            Test for json data
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "Cohort11")
            self.assertTrue(response.content_type == 'application/json')

    def test_json_data_error_response(self):
        """
            Test error message if not json data provided
        """
        response = self.register_user("dian", "dian@gmail.com", "Cohort11")
        data = json.loads(response.data.decode())
        self.assertNotEqual(data.get('message'), "Request should be json")

    def test_json_data_error_response_code(self):
        """
            Test response code if not json data provided
        """
        response = self.register_user("dian", "dian@gmail.com", "Cohort11")
        self.assertNotEqual(response.status_code, 400)

    def test_successful_signup(self):
        """
            Test for successful user signup
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "Cohort11")
            self.assertEqual(response.status_code, 201)

    def test_signup_with_esisting_email(self):
        """
            Tests if User is Registering with an already used email
        """
        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.register_user("boolean", "dian@gmail.com", "Cohort12")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "Email already in use")
            
    def test_existing_user(self):
        """
            Tests for no duplicate user
        """
        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.register_user("dian", "dian@gmail.com", "Cohort11")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "Email already in use")

    def test_invalid_email(self):
        """
            Test for invalid email entry
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "Cohort11")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue('Enter Valid Email ID forexample "sue@gmail.com"' in str(context.exception))
    
    def test_empty_email_field(self):
        """
            Test for empty email field
        """
        with self.client:
            response = self.register_user("dian", "", "Cohort11")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Weak password" in str(context.exception))
    def test_invalid_password(self):
        """
            Test for invalid password
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "Tic")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Weak password" in str(context.exception))
    
    def test_password_length(self):
        """
            Test for password length < 8 characters
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "Tic")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Password must be 8 characters long" in str(context.exception))
    
    def test_if_passsword_has_only_characters(self):
        """
            Test for password has characters only
        """
        with self.client:
            response = self.register_user("dia", "dian@gmail.com", "regards")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Password should have atleast one integer" in str(context.exception))
    
    def test_empty_password_field(self):
        """
            Test for password not provided
        """
        with self.client:
            response = self.register_user("dian", "dian@gmail.com", "")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Field can't be empty" in str(context.exception))
    
    def test_invalid_user_name_length(self):
        """
            Test for invalid name length
        """
        with self.client:
            response = self.register_user("dia", "dian@gmail.com", "Cohort11")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Name too short" in str(context.exception))
    
    def test_invalid_name(self):
        """
            Test for invalid characters 
            in the neme after compilation
        """
        with self.client:
            response = self.register_user("@#$$$$$", "dian@gmail.com", "Cohort11")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Invalid characters not allowed" in str(context.exception))
       
    def test_empty_user_name_field(self):
        """
            Test for empty username field
        """
        with self.client:
            response = self.register_user("", "dian@gmail.com", "Cohort11")
            with self.assertRaises(Exception) as context:
                response
                self.assertTrue("Field can't be empty" in str(context.exception))

    def test_status_code_on_succesful_login(self):
        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.login_user("dian@gmail.com", "Cohort11")
            self.assertEqual(response.status_code, 200)

    def test_message_on_succesful_login(self):
        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.login_user("dian@gmail.com", "Corhot11")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "You have logged in successfully")
    
    def test_login_using_wrong_credentials(self):

        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.login_user("carol@gmail.com", "Cohort12")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "wrong password or email credentials")
            
    def test_if_user_gets_token_on_log_in(self):
        """Test for user login token"""
        with self.client:
            self.register_user("dian", "dian@gmail.com", "Cohort11")
            response = self.login_user("dian@gmail.com", "Cohort11")
            data = json.loads(response.data.decode())
            self.assertTrue(data['token'])
