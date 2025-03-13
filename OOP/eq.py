class Password:
      def __init__(self, data):
            self.data = data
      def __setitem__(self, key, value):
            self.data[key] = value
      
      def __eq__(self, other):
            if isinstance(other, Password):
                  return self.data == other.data
            else:
                  raise TypeError('Error!')
            

users = [
      {
            "username": 'abdulboriyx',
            "password": 2222,
      }
]
usertwo = [
      {
            "username": 'abdulboriyx',
            "password": 2222
      }
]


user1 = Password(users)
user2 = Password(usertwo)

print(user1 == user2)