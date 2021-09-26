import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):

        '''
        testcase  to create an instance of User class.
        '''
        self.new_user = User(password = 'gaidi')


    def test_password_setter(self):
        
        '''
        testcase to  check password is being hashed and the pass_secure 
        
        '''
        self.assertTrue(self.new_user.password is not None)

        

    def test_no_access_password(self):
          
                '''
                testcase to comfirm the application raises Attribute error 
                '''
                with self.assertRaises(AttributeError):
                     self.new_user.password


    def test_password_verification(self):

        '''
        testcase to confirm that password_hash can be verified when a user uses correct password
        '''
        self.assertTrue(self.new_user.password('gaidi'))    