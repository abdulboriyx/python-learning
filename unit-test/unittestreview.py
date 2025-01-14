def main():
      x = int(input('What is x? '))
      result = square(x)
      print('x squared is', result)

def square(y):
      return y + y

if __name__ == "__main__":
    main()