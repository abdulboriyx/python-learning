# while
# i = 0

# while i < 3:
#       print("ooops")
#       i += 1

# i = 1 

# while i <=5: 
#       print("print")
#       i = i * 2

# for
# for i in [0, 1, 2, 3]:
#       print("Hello New World, All the Boyz and Girlz, I have got some true stories to tell, You back outside but they still lied")

# range
# for i in range(10):
#       print("Error")

# print("Error!\n" * 3, end="")

# while True: 
#       n = int(input("What is the n? "))
#       if n > 0: 
#             break

# for _ in range(n): 
#       print("Error!")



def main():
      number = get_number()
      error(number)

def get_number():
      while True:
            n = int(input("What is n? "))
            if n > 0: 
                  return n

def error(n):
      for _ in range(n):
            print("Error!")

main()
