def main():
      greeting = input('Greeting: ').lower()
      greet_bet(greeting)

def greet_bet(str):
      str = str.strip()
      if (str == 'hello'):
            print('0$')
      elif (str[0] == 'h'):
            print('20$')
      else:
            print('100$')

main()