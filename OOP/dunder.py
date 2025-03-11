# class Dunder:
#       def __init__(self, name):
#             self.name = name
            

#       def __str__(self):
#             return f'Hi my name is {self.name}'
#       def __repr__(self):
#             return f'Hi my name is {self.name}'
# name = Dunder('Alex')    
# print(repr(name))
# print(str(name))


# Delete
# class Delete:
#       def __init__(self, name):
#             self.name = name
#             print(f'Name: {self.name}')
#       def __del__(self):
#             print(f'{self.name} is deleted')

# name = Delete('Alex')
# del name

# __new__

class SingletonCar:
    _instance = None

    def __new__(cls, brand, model, year):
        if cls._instance is None:
            # If no instance exists, create it
            cls._instance = super().__new__(cls)
            cls._instance.brand = brand
            cls._instance.model = model
            cls._instance.year = year
        return cls._instance

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Creating instances (but only one instance will be created)
car1 = SingletonCar("Toyota", "Corolla", 2020)
car2 = SingletonCar("Honda", "Civic", 2021)

car1.display_info()  # Output: 2020 Toyota Corolla
car2.display_info()  # Output: 2020 Toyota Corolla (Same instance)

print(car1 is car2)  # Output: True (Same instance)
