import json
with open('for-fun/cars.json', 'r') as file:
      data = json.load(file)
      cars = data['cars']


class Car:
      def __init__(self, name, type, color):
            self.name = name
            self.type = type
            self.color = color
      
      def __str__(self):
            return f'I want to buy {self.color} {self.type} {self.name}'


def main():
      car = get_car()
      print(car)


def get_car():
      name = input('Enter the name of the car: ').lower().strip()
      type = input('Enter the type of the car: ').lower().strip()
      color = input('Enter the color of the car: ').lower().strip()
      

      cars.append({'name': name, 'type': type, 'color': color})  


      with open('for-fun/cars.json', 'w') as file:
            json.dump({'users': cars}, file, indent=4)
            
      return Car(name, type, color)


if __name__ == '__main__':
      main()