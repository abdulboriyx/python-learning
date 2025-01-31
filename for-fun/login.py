import re 
import json


with open('for-fun/users-list.json', 'r') as file:
      data = json.load(file)
      users = data['users'] 

class User:
      def __init__(self, name, email, username, password):
            self.name = name
            self.email = email 
            self.username = username
            self.password = password

      def __str__(self):
            return f'Name is {self.name}, email is {self.email} and username is {self.username}'
            

      # @property
      # def valid_email(self):
      #       return self.email
      
      # @valid_email.setter
      # def valid_email(self, email):
      #       if not re_email(email):
      #             raise ValueError('Invalid email address')
      #       self.email = email
            

def main():
      account_status = input('Do you have account? (Yes/No) ').lower().strip()
      if account_status == 'yes':
            login()
      elif account_status == 'no':
            signup()
      else:
            print('Invalid input!')      



def signup():
      
      sign_name = input('Enter your new name: ').strip().lower()
      sign_email = input('Enter your new email: ').strip().lower()
      sign_user = input('Enter your new username: ').strip()
      sign_password = input('Enter your new password: ').strip()

      if not re_email(sign_email):
            print('Invalid email address! ')
            return
      
      
      if not re_username(sign_user):
            print('Incorrect username!')
            return
      
      for user in users:
            if sign_user == user['username']:
                  print('Username is already taken!')
                  return
      
      
      if not re_password(sign_password):
            print('Incorrect password!')
            return
      
      users.append({'name': sign_name, 'email': sign_email, 'username': sign_user, 'password': sign_password})  


      with open('for-fun/users-list.json', 'w') as file:
        json.dump({'users': users}, file, indent=4)
            
      return User(sign_name, sign_email, sign_user, sign_password)     
      

def login():
      login_username = input('Enter your username: ').strip()
      login_password = input('Enter your password: ').strip()

      for user in users:
        if login_username == user['username'] and login_password == user['password']:
            print('You have logged in successfully!')
            return  # Exit as soon as correct username and password are found
        elif login_username == user['username'] and login_password != user['password']:
            print('Password is incorrect!')
            return  
      print('Username not found!')
            

def re_email(email_regex):
       if re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_regex):
             return True
       else:
             return False
def re_username(username_regex):
      if re.search(r'^!:;,/#@%&*$', username_regex):
            return False
      else:
            return True

def re_password(password_regex):
      if re.search(r'^[A-Z][a-z][0-9](!:.&#$)$', password_regex):
            return True
      else:
            return False


main()


