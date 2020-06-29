class Accounts:
  '''
  Class that generates new instances of accounts
  '''
  accounts_list = []
  
  def __init__(self, account_name,username,password):
          self.account_name = account_name
          self.username = username 
          self.password = password

  def save_account(self): 
        '''
        Method that saves account objects into accounts_list
        '''
        Accounts.accounts_list.append(self)

  def delete_account(self):
      '''
      Method that removes account objects from the accounts_list
      '''
      Accounts.accounts_list.remove(self)

  @classmethod
  def display_all_accounts(cls):
    '''
    Method that returns the accounts list
    '''
    return cls.accounts_list

  @classmethod
  def find_account_name(cls,name):
    '''
    Test case to check if we can find an account
    '''
    for accounts in cls.accounts_list:
      if accounts.account_name == name:
        return accounts

  @classmethod
  def account_exists(cls,name):
   '''
   Method that checks if an account exists
   '''
   for accounts in cls.accounts_list:
     if accounts.account_name == name:
       return True
     return False 


