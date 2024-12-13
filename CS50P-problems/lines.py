import sys

if len(sys.argv) != 2:
      print("Too few or many command-line arguments")

elif not sys.argv[1].endswith('.py'):
      print('No such a file is found')

else:
      print(len(sys.argv))