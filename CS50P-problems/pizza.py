from tabulate import tabulate
import csv
import sys


if len(sys.argv) != 2:
      print("Too few or many arguments! Please check your answer one more time!")
      sys.exit()

elif len(sys.argv) == 2:
      if sys.argv[1].endswith('.csv'):
            with open('regular.csv') as file:
                  reader = csv.reader(file)
                  headers = ['Name', 'Second Column', "Third Column"]
                  menu = tabulate(reader, headers, tablefmt='grid')
                  print(menu)
      else:
            print('No such a file found')
            sys.exit()

