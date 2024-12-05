
# name = input("What is your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file:
#       file.write(f"{name}\n")

# This is one way to read the info on txt file but it is not efficient
# with open("names.txt", "r") as file:
#       lines = file.readlines()
# for line in lines:
#       print("hello,", line.rstrip())

# This is another way and more efficient, neat and conscise way
# with open("names.txt", "r") as file:
#       for line in file:
#             print("hello,", line.rstrip())

names = []

with open("names.txt") as file:
      for line in file:
            names.append(line.strip())
for name in sorted(names):
      print(f"hello, {name}")