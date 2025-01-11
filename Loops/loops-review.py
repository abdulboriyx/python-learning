# while loop

# i = 1
# while i < 5:
#       print('This is loop')
#       i += 1

# x = 0 
# while x < 10:
#       print('Hi! My name is ')
#       x += 1

# your_number = int(input('What is your number? '))

# if your_number < 42:
#       y = your_number
#       while y < 42:
#             print('Life has no meaning!')
#             y += 1

#             if y == 42:
#                   print('This is the meaning of life!')

# for loops

for i in [0, 1, 2]:
      print('Hey')

# for meaning_of_life in range(42):
#       print('Life has no meaning')

# while True:
#       z = int(input('What is your number? '))
#       if z != 42:
#             continue
#       else: 
#             break


# match the club function
# clubs = ['Barcelona', 'Real Madrid', 'Manchester United', 'Manchester City', 'Juventus', 'Arsenal', 'Liverpool']

# def main():
#       your_club = input('What is your club? ')
#       your_team = club_match(your_club)

#       if your_team == None:
#             print('Your club doesn\'t exist in our list')
#       else:
#             print(f'Your club is {your_team}')


# def club_match(team):
#       for club in clubs:
#             if team == club:
#                   return team
#       return None
          

# main()


# len

# movies = ['Interstellar', 'Schindler\'s list', 'Godfather', 'Imitation Game']
# for movie in range(len(movies)):
#       print(movie, movies[movie])

# books = ['O\'tkan Kunlar', 'Mehrobdan Chayon', 'Kod Buzar', 'Ilon Mask']
# for book in range(len(books)):
#       print(book)

# password
# name = input('What is your name? ')
# email = input('What is your email? ')
# password = input('What is your password? ')

# while len(password) < 4:
#       print('Password should contain at least four characters')
#       password = input('What is your password? ')
# print(f'Your name is {name}. Your email is {email}. Your password is {password}')



# ceos = [
#       {'company': 'Google', 'founder(s)': 'Larry & Sergei', 'CEO': 'Sundar Pichai'},
#       {'company': 'Amazon', 'founder(s)': 'Jeff Bezos', 'CEO': 'Andy Cassy'},
#       {'company': 'Apple', 'founder(s)': 'Steve Jobs & Steve Wozniak', 'CEO': 'Tim Cook'},
#       {'company': 'Tesla', 'founder(s)': 'Elon Musk', 'CEO': 'Elon Musk'},
#       {'company': 'Meta', 'founder(s)': 'Mark Zuckerberg', 'CEO': 'Mark Zuckerberg'},
#       {'company': 'Microsoft', 'founder(s)': 'Bill Gates & Paul Allen', 'CEO': 'Satya Nadella'}
# ]
# for ceo in ceos: 
#       print(f'Company: {ceo['company']}, Founder(s): {ceo['founder(s)']}, CEO: {ceo['CEO']}')



users_info = []
while True:
      name = input('Enter your name: ')
      email = input('Enter your email: ')
      password = input('Enter your password: ')


      user_data = {
            'name': name,
            'email': email,
            'password': password
      }

      users_info.append(user_data)

      another_user = input('Do you want to enter another user? (yes or no): ').lower()
      if another_user != 'yes':
            break


def main():
      searched_name = input('Enter the name you want to get info about: ')
      search_name = get_name(searched_name)

      if search_name == None:
            print('User not found')
      else:
            print(f'User is found. User\'s name: {search_name['name']}, user\'s email: {search_name['email']}')

def get_name(name):
      for user in users_info:
            if name == user['name']:
                  return user
      return None

main()










