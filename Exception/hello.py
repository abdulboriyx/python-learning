def main():
      x = get_int("What is x? ")
      print(f"X is {x}")

def get_int(prompt):
      while 0 < 1: 
            try:
                  # x = int(input("What is x? "))
                  return int(input(prompt)) # it is possible to totally remove the "else" block and put everything inside "try" block, but you gotta do it consciously not 'just because it works'
            except ValueError:
                  pass
                  # print(f"Error! X is not integer!") 
            # else:
                  # return x #'break' is also option but to be more concise, 'return' does the same thing as 'break' did


main()