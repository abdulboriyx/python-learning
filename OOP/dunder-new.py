class SingleCar:
      _instance = None

      def __new__(cls, brand, model):
            if cls._instance is None:
                  cls._instance = super().__new__(cls)
                  cls._instance.brand = brand
                  cls._instance.model = model
            return cls._instance

      def display_info(self):
            print(f'{self.model} is produced by {self.brand}')

tesla = SingleCar('Tesla', 'Model Y')
rolls_royce = SingleCar('Rolls Royce', 'Phantom')

tesla.display_info()
rolls_royce.display_info()