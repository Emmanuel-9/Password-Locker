class User:
  '''
  Class that generates new instances of users
  '''

  usersList = []

  def __init__(self,username,password):
    '''
    Defining attributes of the class
    '''
    self.username = username 
    self.password = password

  def save_users(self):
    '''
    Saving users to usersList
    '''
    User.usersList.append(self)
  