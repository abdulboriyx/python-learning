import csv 
import sys

table = []

with open('before.csv') as file: 
      reader = csv.DictReader(file)
      for row in reader:
            name = row['name'].strip()
            house = row['house'].strip()

            first_name, last_name = name.split(',')
            table.append({'first': first_name, "house": house})

for col in table:
      print(f"{col['first']} is in {col['house']}")