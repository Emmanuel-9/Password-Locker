import unittest
from users import User

class TestUsers(unittest.TestCase):
    '''
    Test class defininig the test cases for class Users
    '''
    def setUp(self): 
        '''
        Method before test cases 
        '''
        self.new_user = User("Job","0786")

    def test_init_(self):
        '''
        Test case to check if objects are initialized well
        '''
        self.assertEqual(self.new_user.username,"Job")
        self.assertEqual(self.new_user.password,"0786")    

