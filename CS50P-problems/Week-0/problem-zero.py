# tip 
def main():
      total_check = check_to_float(input('How much was the food?: '))
      tip_percent = percent_to_float(input('What percenateg would you like to tip?: '))
      total_tip = total_check * tip_percent
      print(f'Leave ${total_tip:.3f}')

def check_to_float(check):
      check = check.replace("$", "")
      check = float(check)
      return check

def percent_to_float(percent):
      percent = percent.replace("%", "")
      percent = float(percent)
      percent = percent/100
      return percent

main()