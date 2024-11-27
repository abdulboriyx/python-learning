import sys
import statistics

# print(statistics.mean([100, 70, 10, 11110, 223]))

# try:
#       print (sys.argv[1])
# except IndexError:
#       print("Error, You idiot!")



if len(sys.argv) < 2:
      sys.exit("Error! Too few arguments!")
# elif len(sys.argv) > 2: 
#       sys.exit("Error! Too many arguments!")
# else: 
for arg in sys.argv[1:]: # this literally means slice the first element & print everything remaining
      if arg == "Drake":
            sys.exit("Bruhh, Drake is not GOAT")
      else:
            print(arg, "is the GOAT")