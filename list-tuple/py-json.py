import json

try:
      with open('list-tuple/list.json', 'r') as file:
            data = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    data = []


insert_name = input('What is your name?: ')
insert_age = int(input('What is your age?: '))
insert_city = input('Where are you from?: ')

user_exist = any(user["username"] == insert_name for user in data)


if user_exist:
      print('Account exists!')
else:
      data.append({"username": insert_name, "age": insert_age, "city": insert_city})

with open('list-tuple/list.json', 'w') as file:
    json.dump(data, file, indent=2)








