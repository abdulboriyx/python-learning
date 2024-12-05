name = input("What is your name? ")

file = open("io-names.txt", "a")
file.write(f"{name}\n")

file.close()

# This code is good but we can make it better with literally


# This is for writing
name = input("Enter your name: ")
email = input("Enter your email: ")
country = input("Enter your country: ")

with open("io-names.txt", "a") as file:
      file.write(f"Your name is: {name}; \nYour email is: {email};\nYou are from {country}\n")

# This is for reading a file

with open("io-names.txt", 'r') as file:
      texts = file.readlines()

for text in texts:
      print("Wassup homie?", text)

# nardwuar programm

who_ru = input("Who are you? ")
with open("rapname.txt", "a") as file:
      file.write(f"{who_ru}\n")

# This is precise & cool way to save
rappers_name = []

with open("rapname.txt", "r") as file:
      for rapper in file:
            rappers_name.append(rapper.rstrip())
for rapper in sorted(rappers_name):
      print(f"Who are you? I am {rapper}")