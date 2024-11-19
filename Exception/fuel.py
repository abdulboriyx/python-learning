import math

def main():
      f = get_fuel()

      
      if f <= 1:
            print("E")
      elif f >= 99:
            print("F")
      else:
            print(f"{f}%")
                 

def get_fuel():
      while True:
            try:
                  x = int(input("What is x? "))
                  y = int(input("What is y? "))
                  

                  if x > y:
                        print("Error!")
                        continue
                  fuel_q = math.ceil((x/y) * 100)
                  
                  return fuel_q
            except (ValueError, ZeroDivisionError):
                  pass
           
            
main()