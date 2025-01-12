try:
      z = int(input('What is Z? '))
      
except ValueError:
      print('Z is not ineger. Check your answer and enter integer')
      z = int(input('What is Z? '))

print(f'Z is {z}')


def main():
      x = get_int()
      print(f'x is {x}')

def get_int():
      while True:
            try:
                 return int(input('What is X? '))
            except ValueError:
                 print('X is not integer!')
                 pass 
      

main()


