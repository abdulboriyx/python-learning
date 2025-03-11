class DateCalc:
      def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year


      def __sub__(self, other):
            if not isinstance(other, type(self)):
                  raise TypeError('Error!')
            else:
                  total_self = (self.year * 365) + (self.month * 30) + (self.day)
                  total_other = (other.year * 365) + (other.month * 30) + (other.day)

                  if (total_self > total_other):
                        total_difference = total_self - total_other
                  elif (total_self < total_other):
                        total_difference = total_other - total_self
                  
                  diff_year = total_difference // 365
                  remaining_day = total_difference % 365
                  diff_month = remaining_day // 30
                  diff_day = remaining_day % 30
            
            return DateCalc(diff_day, diff_month, diff_year)
      
      def __str__(self):
            return f'Difference between two dates: {self.day} days, {self.month} months, {self.year} years.\n {self.month} months\n {self.day} days'

            
      
      

calc = DateCalc(11, 6, 2025)
calc0 = DateCalc(22, 4, 2022)
calc1 = calc - calc0
print(calc1)