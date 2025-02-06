def main():
      enter_expression = input('Expression: ')
      get_expression(enter_expression)

def get_expression(zet):

      x, y, z = zet.split(' ')
      x = float(x)
      z = float(z)
      if (y=="+"):
            print(x+z)
      elif (y=="-"):
            print(x-z)
      elif (y=="*"):
            print(x*z)
      else:
            print(x/z)

main()