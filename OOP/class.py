class Car:
      type_car = "Luxury SUV"
      def __init__(self, name, company):
            self.name = name
            self.company = company
      
      def description(self):
            return f'{self.name} is {self.type_car} and produced by {self.company}'
      # def __str__(self):
      #       return f'{self.name} is {self.type_car} and produced by {self.company}'
      
      def performance(self, speed, energy):
            return f'{self.name}\'s max speed is {speed} and uses {energy}l for 100 km'

rr_cullinan = Car('Rolls Royce Cullinan', 'Rolls Royce')
b_bentayga = Car('Bentley Bentayga', 'Bentley')
m_levante = Car('Maserati Levante', 'Maserati') 



print(rr_cullinan)


