import json



# Ensure the correct path to the file, adjust if necessary
with open('for-fun/user-list.json', 'r') as file:
    data = json.load(file)
    users = data["users"]

def main():
    account_question = input('Do you have account? yes/no ').lower()
    
    if account_question == 'yes':
        your_username = input('Enter your username: ')
        your_password = input('Enter your password: ')
        result = log_in(your_username, your_password)
        if result:
            print(f'User is found: {result["username"]}. Password is correct')
        else:
            print('User is not found')
    
    elif account_question == 'no':
        new_username = input('Enter username: ')
        new_password = input('Enter password: ')

        for user in users:
            if new_username == user['username']:
                print('Username already exists! Please try a different one.')
                return
        
         # Append new user to the list
        users.append({'username': new_username, 'password': new_password})
        print('Signup successful!')

        # Save updated data back to the JSON file
        data["users"] = users  # Update the 'users' key in the data dictionary
        with open('for-fun/user-list.json', 'w') as file:
            json.dump(data, file, indent=4)  

def log_in(username, password):
    for user in users:
        if username == user['username']:
            if password == user['password']:
                return user
            else:
                return f'User is found: {username}. Password is wrong, try again.'
    return False

main()
