import re

email = input("What is your email address? ")

if re.search(r'^\w+@(\w+\.)?\w+\.edu$' , email, re.IGNORECASE):
      print('Valid')
else: 
      print('Invalid')