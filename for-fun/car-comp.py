

class CarComp:
      def __init__(self):
            self.data = {}

      def __getitem__(self, key):
           return self.data[key]
cars = [{  
      "car": 'Rolls Royce', 
      "horsepower": 563,
      "speed": 250,
    },
{
    "car": 'Porsche 911',
    "horsepower": 388,
    "speed": 308       
}
]

car_dict = CarComp()
car_dict.data = cars

your_car = input('What is your car? ')
yourcar_hp = int(input('What is horsepower of your car? '))
yourcar_speed = int(input('What is max speed of your car? '))
for car in car_dict.data:
      print(f"{car['car']} vs {your_car};\n Max Speed: {car['speed']} vs {yourcar_speed};\n HP: {car['horsepower']} vs {yourcar_hp}")
