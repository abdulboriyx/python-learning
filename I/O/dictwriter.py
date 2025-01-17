import csv


# company = input('Enter the company name: ')
# founder = input('Enter the founder name: ')
# year = input("Enter the year company founded: ")

# with open('I/O/csv-list.csv', 'a') as file:
#       writer = csv.DictWriter(file, fieldnames=["company", "founder", "year"])
#       writer.writerow({'company': company, 'founder': founder, 'year': year})


# signup & login

name = input('Enter your name: ')
email = input('Enter your email: ')
password = input('Enter your password: ')
username = input('Enter your username: ')


with open('I/O/login.csv', 'a') as file:
      writer = csv.DictWriter(file, fieldnames=["name", "email", "password", "username"])
      writer.writerow({'name': name, 'email': email, 'password': password, 'username': username})
      


