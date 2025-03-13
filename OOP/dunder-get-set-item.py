class List:
      def __init__(self, elements):
            self.elements = elements
      
      def __getitem__(self, index):
            return self.elements[index]
your_car = input('What is your car? ')
car_brands = List(['Aston Martin Vintage', 'Porsche 911', 'Tesla Model Y'])
for car in car_brands:
      print(f'{your_car} vs {car}')


# artist
class Artists:
      def __init__(self, elements):
            self.elements = elements
      
      def __getitem__(self, index):
            return self.elements[index]

      
            
artists = [
      {
            "name": "Kendrick Lamar",
            "genre": "Hip-Hop"
      }, 
      {
            "name": "Tyler",
            "genre": "Hip-Hop"
      }, 
      {
            "name": "Jay-Z",
            "genre": "Hip-Hop"
      }, 
      {
            "name": "The Weeknd",
            "genre": "Pop"
      }
]
artists_list = Artists(artists)

for artist in artists_list:
      if (artist['genre'] == 'Hip-Hop'):
            print(f'{artist['name']} is Hip-Hop artist')
      elif (artist['genre'] != 'Hip-Hop'):
            print(f'{artist['name']} is {artist['genre']} artist!')

