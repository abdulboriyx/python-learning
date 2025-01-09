club = input('What is your club? ')

# .strip() built-in function strips away whitespace on your user's response 
club = club.strip().title()
print('Your club is', club)


# string

x = int(input('What is your X? '))
y = int(input('What is your Y? '))

z = x + y 
print(z)


# float 
x = float(input('What is your X? '))
y = float(input('What is your Y? '))

z = round((x + y), 1)
print(z)


# function

def hello():
      print('hello')

username = input('What is your username? ')
hello()
print(username)

# variable in function 

username = input('What is your username? ')

def hello(user):
      print('Hello,', user)
hello(username)

def goodbye(user): 
      print('Goodbye,', user)
goodbye(username)

def hello(user='user'):
      print('Hello,', user)

hello(username)
hello()


# return()
def main():
     calculator = calculate(34, 2)
     print(calculator)


def calculate(x, y):
      return int(x / y) 



main()

