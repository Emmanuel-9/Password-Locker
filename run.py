#!/usr/bin/env python3.8
from accounts import Accounts
import string, random 
from users import User

def add_account(account,user_name,password):
  '''
  Function to add new account details 
  '''
  new_account = Accounts(account,user_name,password)
  return new_account

def save_accounts(accounts):
  '''
  Function to save contact
  '''
  accounts.save_account()

def delete_accounts(accounts):
  '''
  Function to delete an account
  '''
  accounts.delete_account()

def find_account(name):
  '''
  Function that finds an account by account-name and returns the account
  '''
  return Accounts.find_account_name(name)

def view_existing_accounts(name):
  '''
  Function that check if an account exists with account name and return a boolean
  '''
  return Accounts.account_exists(name)

def display_accounts():
  '''
  Function that returns all saved 
  '''
  return Accounts.display_all_accounts() 

def generatePassword(num):
  password = ' '

  for random in range(num):
    selected = random.randint(0,94)
    password += string.printable[selected]

  return password

def create_locAccount(username,password):
  '''
  Function to create appliction login account
  '''
  new_user = User(username,password)
  return new_user

def save_user(user):
  '''
  Saving user
  '''
  user.save_users()

def main():
  print("Hi there, welcome to password-Lock. Please create an account")
  print('\n')

  username = input("Enter Password-Lock username: ")
  password = input("Type in your password: ")
  
  print(f"Hello {username}. Please type in your password to continue")
  print('\n')

  password_confrim = input("Type password: ")

  while password_confrim == password:
    save_user(create_locAccount(username,password))

    print("Awesome! Select from the short-code options: ca - create new account details, ac - Add new account details, da - display accounts saved, dl - delete an account record, lo - log out of Password-Loc account")

    option = input().lower()

    if option == 'ac':
      print("Add Account details")
      print("-"*10)

      print("Account name: ")
      account = input()
      print("Account's username: ")
      user_name = input()
      print("Acount's password")
      password = input()

      save_accounts(add_account(account,user_name,password)) 
      print ('\n')
      print(f"New Account {account} added")
      print ('\n')  

    elif option == 'ca':
      print("New Account details")
      print("-"*10)

      print("Account name: ")
      account = input()
      print("Account's username: ")
      user_name = input()
      print("Acount's password")
      password = generatePassword(12)
      print(f"Your account_password will be {password}")
      length_of_password = len(password)
      print(f"Password is {length_of_password} characters long.")

      save_accounts(add_account(account,user_name,password)) 
      print ('\n')
      print(f"New Account {account} added")
      print ('\n')  

    elif option == "da":
      if display_accounts():
          print("These are the accounts saved currently.")
          print('\n')

          for account in display_accounts():
            print(f"{account.account_name} {account.username} .....{account.password}")

            print('\n')
      else:
        print('\n')
        print("No accounts added so far!")
        print('\n')

    

    elif option == 'dl':
      print("Enter the account name you wish to delete: ")

      search_name = input()
      if view_existing_accounts(search_name):
        search_account = find_account(search_name)
        print(f"You prompted to delete {search_account.account_name} account. \n Continue? [y/n]")

        confirm = input()
        if confirm == 'y':
          delete_accounts(search_account)
          print('-' * 20)

          print(f"Account.......{search_account.account_name} has been deleted.")
        else:
          print("Action Aborted!")

    elif option == "lo":
      print("Logging out .......")
      break
    else:

      print("Wrong short code option! Please look at the short codes again!")   

if __name__ == '__main__':
  main()