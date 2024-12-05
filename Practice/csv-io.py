import csv
# with open("rapname.csv") as file:
#       for rapper in file:
#             row = rapper.rstrip().split(",")
#             print(f"{row[0]} is from {row[1]}" )
# As usual, this can be done a bit consice and beautiful, I would say

# with open("rapname.csv") as file:
#       for rapper in file:
#             name, city = rapper.rstrip().split(",")
#             print(f"{name} is from {city}")

# rappers_list = []

# with open("rapname.csv") as file:
#       for line in file:
#             name, city = line.rstrip().split(",")
#             rapper = {rapper["name"]: name, rapper['city']: city}
#             rappers_list.append(rapper)
# for rapper in sorted(rappers_list, key=lambda rapper: rapper['name']):
#       print(f"{rapper["name"]} is from {rapper["city"]}")

# I cant input more than two values, how to solve it?

laliga_standing = []

with open("laliga-standing.csv") as file:
      reader = csv.DictReader(file)
      for row in reader:
            laliga_standing.append({"club": row["club"], "stats": row["stats"]})

for standing in laliga_standing:
      print(f"{standing['club']}'s stats are {standing['stats']}")
 