# __add__

class Addition:
      def __init__(self, x):
            self.x = x 

      def __add__(self, other):
            return Addition(self.x + other.x)
      def __repr__(self):
            return f'Addition({self.x})'

addition1 = Addition(1)
addition2 = Addition(2)

addition3 = addition1 + addition2
print(addition3)


class LondonCollege:
      def __init__(self, tuition, living_cost, rent):
            self.tuition = tuition
            self.living_cost = living_cost
            self.rent = rent
      def __add__(self, other):
            return LondonCollege(self.tuition + other.tuition, self.living_cost + other.living_cost, self.rent + other.rent)
      def __str__(self):
            return f'Tuition: {self.tuition}; Living cost: {self.living_cost}; Rent: {self.rent}'

mine = LondonCollege(35000, 1000, 1600)
gf = LondonCollege(45000, 1200, 1600)

all_expense = mine + gf 
print(all_expense)


# isinstance
class Spending:
      def __init__(self, clothes, watch):
            self.clothes = clothes
            self.watch = watch

      def __add__(self, other):
            if isinstance(other, type(self)):
                  return Spending(self.clothes + other.clothes, self.watch + other.watch)
            else:
                  raise TypeError('Error input! Please check your input')
      
      def __str__(self):
            return f'Clothes expense: ${self.clothes}; Watch expense: ${self.watch}'
      
lv_cartier = Spending(250, 7750)
rl_ap = Spending(165, 4500)
all_spending = lv_cartier + rl_ap

print(all_spending)


# sub
class CalendarCalc:
      def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day
      def __sub__(self, other):
            if isinstance(other, type(self)):
                  return CalendarCalc(self.year - other.year, self.month - other.month, self.day - other.day)
            else:
                  raise TypeError('Incorrect input! Check your Answer')
      
      def __str__(self):
            return f'Difference is {self.year} year(s), {self.month} month(s), {self.day} day(s)'
      


arrival_date = CalendarCalc(2022, 8, 11)
today = CalendarCalc(2025, 3, 7)
calculated = arrival_date - today
print(calculated)
            