import re
import json

with open('for-fun/sale-car.json', 'r') as file:
      data = json.load(file)
      salecars = data['salecar']
      
class Sell:
      def __init__(self, name, year, color, price):
            if not name:
                  raise ValueError('Missing name')
            self.name = name
            self.year = year
            self.color = color 
            self.price = price


      @classmethod
      def sale_car(cls):
            name = input('Enter your name: ')
            year = input('Enter car\'s year: ')
            color = input('Enter color: ')
            price = input('Enter price: ')
                 
            salecars.append({'name': name, 'year': year, 'color': color, 'price': price})

            with open('for-fun/sale-car.json', 'w') as file:
                  json.dump({'salecar': salecars}, file, indent=4)

            return cls(name, year, color, price)
      
      def __str__(self):
            return f'You want to sell {self.year} {self.color} {self.name} for {self.price}. We added it to our list. We will contact you as soon as we find client for your car. Thank You'    

def main():
      car_sale = Sell.sale_car()
      print(car_sale)


if __name__ == '__main__':
      main()