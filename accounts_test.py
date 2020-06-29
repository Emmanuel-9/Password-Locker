import unittest
from accounts import Accounts

class TestAccounts(unittest.TestCase):
    '''
    Class for the test cases of class Accounts
    '''

    def setUp(self):
        '''
        Method that runs before the test cases
        '''
        self.new_account = Accounts("Facebook","Cliff","pass1234")

    def test__init__(self):
        '''
        Testing whether the object is initialized well
        '''
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.username,"Cliff")
        self.assertEqual(self.new_account.password,"pass1234")

    def test_save_account(self):
        '''
        Test case for saving contacts
        '''
        self.new_account.save_account()
        self.assertEqual(len(Accounts.accounts_list),1)   

    def tearDown(self):  
        '''
        Method that cleans up after each test case
        '''
        Accounts.accounts_list = []

    def test_save_multiple_accounts(self):
        '''
        Test case for saving several contacts to accounts_list
        '''
        self.new_account.save_account()
        second_account = Accounts("Snapchat","Rozzy","4321")
        second_account.save_account()
        self.assertEqual(len(Accounts.accounts_list),2)

    def test_delete_account(self):
        '''
        Testing the removal of an account from the accounts_list
        '''
        self.new_account.save_account()
        second_account = Accounts("Snapchat","Rozzy","4321")
        second_account.save_account()
        second_account.delete_account()
        self.assertEqual(len(Accounts.accounts_list),1)

    def test_display_all_accounts(self): 
        '''
        Method to test whether the accounts in the list can be dislayed
        '''
        self.assertEqual(Accounts.display_all_accounts(),Accounts.accounts_list)    
     
    def test_find_account_name(self):
        self.new_account.save_account()
        second_account = Accounts("Snapchat","Rozzy","4321")
        second_account.save_account()
        found_account = second_account.find_account_name("Snapchat")
        self.assertEqual(found_account.username,second_account.username)

    def test_check_account(self):
        '''
        Test case to check if we can  return a boolean if we cannot find the account
        '''
        self.new_account.save_account()
        second_account = Accounts("Snapchat","Rozzy","4321")
        second_account.save_account()
        account_exists = Accounts.account_exists("Snaochat")

        self.assertTrue(account_exists)

if __name__ == '__main__':
    unittest.main()