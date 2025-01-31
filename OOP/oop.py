import random

# def main():
#       exec = get_exec()
#       print(f'{exec[0]} is CEO of {exec[1]}')

# def get_exec():
#       ceo = input('Enter the name of CEO: ')
#       company = input('Enter the name of the company: ')
#       return (ceo, company) # this is tuple 

# if __name__ == '__main__':
#       main()


# country and capital
# def main():
#       country = get_country()
#       if country[0] == 'South Korea':
#             country[1] = 'Seoul'

# def get_country():
#       republic = input('Enter the Republic name: ')
#       capital = input('Enter the capital name: ')
#       return(republic, capital)

# if __name__ == '__main__':
#       main()



# same the above but with dict
# def main():
#       country = get_country()
#       if country['name'] == 'South Korea':
#             country['capital'] = 'Seoul'
#       print(f'{country['capital']} is capital of {country['name']}')

# def get_country():
#       country = {}
#       country['name'] = input('Enter the name of the country: ')
#       country['capital'] = input('Enter the capital: ')
#       return {'name': country['name'], 'capital': country['capital']}

# main()


# class
# class Student:
#       def __init__(self, name, house):
#             self.name = name
#             self.house = house


# def main():
#       student = get_student()
#       print(f'{student.name} is capital of {student.house}')

# def get_student():
#       name = input('What is your name? ')
#       house = input('What is your house? ')
#       student = Student(name, house)
#       return student  
# 



# coffeeshop


# class Coffee:
#       def __init__(self, name, size, type, brand):
#             if not name:
#                   raise ValueError('Missing coffee name')
#             self.name = name
#             self.size = size
#             self.type = type
#             self.brand = brand
#       def __str__(self):
#             return f'{self.type} {self.name} {self.size}, please'
      

#       @property
#       def coffee_chain(self):
#             return self.name
      
#       @coffee_chain.setter
#       def coffee_chain(self, name):
#             if name not in ['Americano', 'Latte', 'Cappucino']:
#                   raise ValueError('Invalid Coffee')
#             self.name = name

      
   

# def main():
#       coffee = get_coffee()
#       coffee.coffee_chain = 'Brew'
#       print(coffee)
      
      

# def get_coffee():
#       name = input('Enter coffee name: ').strip()
#       size = input('Enter coffe size: ').strip()
#       type = input('Do you want hot or ice? Hot/Iced ').lower().strip()
#       brand = input('Enter coffee brand: ')
#       return Coffee(name, size, type, brand)

# if __name__ == '__main__':
#       main()



# class Hat:
#       def __init__(self):
#             self.clubs = ['Barcelona', 'Juventus', 'Real Madrid', 'PSG', 'Manchester United']

#       def sort(self, name):
#             print(f'{name} to {random.choice(self.clubs)}! Here we go!')

# hat = Hat()
# hat.sort('Harry Maguire')


# random_gate = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# random_city = random.choice(['Katta Qo\'rg\'on', 'Narpay', 'Yangiobod', 'Uchquduq', 'Beshariq', 'Dargom'])

# class City:

      
#       cities = ['Barcelona', 'London', 'Seoul', 'Tokyo', 'Mecca']
      

#       @classmethod
#       def get_city(cls, city):
            
#             print(f'Boarding for {city} - {random.choice(cls.cities)} is started. Please go to Gate {random_gate}')

# City.get_city(random_city)


# inheritance

# class Philosophy:
#       def __init__(self, name):
#             if not name:
#                   raise ValueError('Missing name!')   
#             self.name = name

# class Stoicisim(Philosophy):
#       def __init__(self, name, key_figure):
#             super().__init__(name)
#             self.key_figure = key_figure

# class Hedonism(Philosophy):
#       def __init__(self, name, idea):
#             super().__init__(name)
#             self.idea = idea


class Luggage:
      def __init__(self, books=0, pencils=0, pens=0):
            self.books = books
            self.pencils = pencils
            self.pens = pens

      def __str__(self):
            return f'There are {self.books} books, {self.pencils} pencils and {self.pens} pens on luggage'

      def __add__(self, other):
            books = self.books + other.books
            pencils = self.pencils + other.pencils
            pens = self.pens + other.pens
            return Luggage(books, pencils, pens)

cargo_zero = Luggage(10, 1, 3)
print(cargo_zero)

cargo_one = Luggage(8, 4, 1)
print(cargo_one)

total = cargo_one + cargo_zero
print(total)