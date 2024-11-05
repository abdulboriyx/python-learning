# name = input("What is your name? ")
# print("hello," + name)
# print("hello", name, sep="-")

# quote inside quote
# print("hello, \"friend\"")

# chosen text

# name = input("What is your name? ").strip().title()
# print(f"hello, {name}")


# def

# def hello(to="World"):
#       print("hello,", to)

# hello()
# name = input("What is your name? ")
# hello(name)

# def func():
#       print("Hello, world!")

# func()

def greet(input):
      if "hello" in input:
            return "Hello, there"
      else:
            return "I am not sure what you are saying"

greeting = greet("hello")
print(greeting + " world")