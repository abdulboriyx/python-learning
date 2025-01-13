import random 
import requests
import sys
import json

# Random
goat = random.choice(['Messi', 'Ronaldo'])
print(f'Goat is {goat}')

random_number = random.randint(1, 99)
print(random_number)


# your random favourite artist
artist_list = []

while True:
      enter_artist = input('Enter your favourite artist: ')
      artist_list.append(enter_artist)

      another_artist = input('Do you want to add more artist(s)? (yes/no) ').lower()
      if another_artist != 'yes':
            break

random_artist = random.choice(artist_list)

print(f'Your random favuorite artist is {random_artist}')

############################################################



# sys.argv



try: 
      print('Your name is', sys.argv[1])
except IndexError:
      print('Too few arguments')


users = [
      {'username': 'abdulboriyx', 'password': 'rais1202!'},
      {'username': 'raxmatillo_', 'password': 'tillo2557'}, 
      {'username': 'xojiakbar_anvarovich', 'password': 'jojo1234'}
]



for user in users:
      if sys.argv[1] == user['username']:
            print(f'username is found: {user['username']}')
            break
      else:
            print('Username is not found')
            

for user in users:
      if sys.argv[1] != user['password']:
            sys.exit('Incorrect password!')
      else:
            print('You entered correct password')

############################################################

# slice

if len(sys.argv) < 2:
      sys.exit('Too few arguments!')
for arg in sys.argv[1:]:
      print('Hello my name is', arg)

############################################################

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/" + sys.argv[1])

if response.status_code == 200:
    fact = response.json()
    print(fact['text'])
else:
    print('Error!')
