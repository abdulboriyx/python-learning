# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# \ -> literally the character follows
# [a-zA-z0-9_] = \w
# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

import re

# email = input('What is your email?: ').strip()

# if re.search(r'^\w+@\w+\.(com|edu|net|hotmail)$', email, re.IGNORECASE):
#       print(f'Valid email. Your email is {email}')
# else:
#       print('Invalid value')

# text = input('Enter your email: ').strip()

# matches = re.search(r'^(.+) (.+)$', text)

# if matches:
#       text = matches.group(2) + " " + matches.group(1)
#       print(matches.group(1))



# credit card

credit_card = input('Enter your credit card number: ').strip()
if re.search(r'(\d{4}\s?\d{4}\s?\d{4}\s?\d{4})', credit_card):
      print('Valid')
else:
      print('Invalid input')
      
