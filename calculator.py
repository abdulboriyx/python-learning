# x = input("What is x? ")
# y = input("What is y? ")

# z = int(x) + int(y)

# print(z)

# shorter
# x = int(input("What is x? "))
# y = int(input("What is y? "))

# print(x + y)

# float
# x = round(float(input("What is x? ")))
# y = round(float(input("What is y? ")))
# print(x + y)

# number formatting
# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = round(x + y)

# print(f"{z:,}")

# division

# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = round(x / y, 2) 

# print(z)

def main():
      x = int(input("What's x? "))
      print("x squared is", square(x))

def square(n):
      return n * n


main()

