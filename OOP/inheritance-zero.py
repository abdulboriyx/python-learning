class Iphone15:
      def __init__(self, type, cpu, memory, camera):
            self.type = type
            self.cpu = cpu
            self.memory = memory
            self.camera = camera

      def features(self):
            return f'{self.type} is out now! It has {self.cpu} CPU; {self.memory} GB RAM; Its camera is {self.camera}MP (main)'
      
class Iphone15Pro(Iphone15):
      def __init__(self, type, cpu, memory, camera, lena):
            super().__init__(type, cpu, memory, camera)
            self.lena = lena
      def features(self):
            # return super().features()
            return f'{self.type} is out now! It has {self.cpu} CPU; {self.memory} GB RAM; Its camera is {self.camera}MP (main) + {self.type} offers {self.lena} camera'
class Iphone15ProMax(Iphone15):
      def __init__(self, type, cpu, memory, camera, lena, battery):
            super().__init__(type, cpu, memory, camera)
            self.lena = lena
            self.battery = battery
      def features(self):
            # return super().features()
            return f'{self.type} is out now! It has {self.cpu} CPU; {self.memory} GB RAM; Its camera is {self.camera}MP (main) + {self.type} offers {self.lena} camera + {self.battery}'


iphone15 = Iphone15('Iphone 15', 'A16 Bionic', 6, 48)
iphone15pro = Iphone15Pro('Iphone 15 Pro', 'A17 Pro Chip', 8, 48, '3x zoom')       
iphone15promax = Iphone15ProMax('Iphone 15 Pro Max', 'A17 Pro', 8, 48, '5x zoom', 'Longer battery life')

print(iphone15.features())
print(iphone15pro.features())
print(iphone15promax.features())