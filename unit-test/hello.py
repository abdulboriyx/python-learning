def main():
      name = input('What is your name? ')
      hi_func(name)

def hi_func(to='world'):
      return f'hello, {to}'


if __name__ == "__main__":
    main()