def main():
      time = input('What time is it?: ')
      time = convert(time)

      if (7.0<=time<=8.0):
            print('Breakfast')
      elif (12.0<=time<=13.0):
            print('Lunch')
      elif (18.0<=19.0):
            print('Dinner')
      else:
            print('Unknown')

def convert(meal_float):

      hours, minutes = meal_float.split(":")
      hours = float(hours)
      minutes = float(minutes)
      times = hours + minutes/60 
      return times


main()