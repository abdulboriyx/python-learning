import re
# email = input('What is your email? ').strip()

# username, domain = email.split('@')

# if username and '.' in domain:
#       print(f'Valid, your email is {email}')
# else: 
#       print('Invalid. Enter correct email address')

# if re.search('.+@.+', email):
#       print(f'Valid. Your email is {email}')
# else:
#       print('Invalid')

#  \ escaping character and regex accept anything after that as special character, not anything

# if re.search(r'^.+@.+\..+$', email):
#       print(f'Valid. Your email is {email}')
# else:
#       print('Invalid. Enter correct email address')


# except -> [^]

# if re.search(r'^[^@]+@[^@]+\.com$', email):
#       print(f'Valid. Your email is {email}')
# else:
#       print('Invalid. Enter correct email address')


# [set of characters]

# if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$', email):
#       print(f'Valid. Your email address is {email}')
# else:
#       print('Invalid. Enter correct email address.')

# \w means the same as [a-zA-Z0-9_]

# if re.search(r'^\w+@\w+\.com', email):
#       print(f'Valid. Your email is {email}')
# else:
#       print('Invalid. Enter correct email address')

# if re.search(r'^\w+@\w+\.(com|edu|net|org|hotmail)$', email):
#       print(f'Valid. Your email is {email}')
# else:
#       print('Invalid. Enter correct email address')



# case sensitivty

# if re.search(r'^\w+@\w+\.(com|edu|net|org|hotmail)$', email, re.IGNORECASE):
#       print(f'Valid. Your email address is {email}')
# else:
#       print('Invalid. Enter correct email address')

# ? -> optional

# if re.search(r'^\w+@(\w+\.)?\w+\.(com|edu|net|org)$', email, re.IGNORECASE):
#       print(f'Valid. Your email address is {email}')
# else:
#       print('Invalid. Enter correct address')

# Cleaning the user input

# name = input('What is your name? ').strip()

# if ',' in name:
#       last, first = name.split(',') 
#       name = f'{first} {last}'
# print(f'hello, {name}') 

# matches
# * -> 0|1

# matches = re.search(r'^(.+), *(.+)$', name)
# if matches:
#       last, first = matches.groups()
#       name = first + " " + last

# print(f'hello, {name}')


# Extracting User Input
# url = input("URL: ").strip()
# print(f'Your url is {url}')

# replace

url = input('URL: ').strip()
# username = url.removeprefix('https://www.instagram.com/')
# print(f'Username: {username}')

# username = re.sub(r'https://twitter.com/', "", url)
# print(f'Username: {username}')


username = re.sub(r'^(https?://)?(www\.)?twitter\.com/', "", url)
print(f'Username: {username}')