import json

soccer_teams = {
      "Milan": ['Inter Milan', 'Milan'],
      "London": ['Arsenal', 'Chelsea', 'Tottenham Hotspur', 'West Ham', 'Crystal Palace'],
      'Madrid': ['Atletico Madrid', 'Getafe CF', 'CD Leganes', 'Rayo Vallecano', 'Real Madrid'],
      "Barcelona": ['Barcelona', 'Espanyol'],
      "Turin": ['Juventus', 'Torino']
}
try:  
     with open('list-tuple/pys.json', 'r') as file:
            soccer_data = json.load(file)
      
except (FileNotFoundError, json.JSONDecodeError):
      soccer_data = []

your_city = input('Enter your city name: ')

if your_city in soccer_data:
      your_club = input('Enter your club: ')

      if your_club not in soccer_data[your_city]:
            soccer_data[your_city].append(your_club)
      elif your_club in soccer_data[your_city]:
            print(f'{your_club} is already entered')
      

elif your_city not in soccer_data:
      your_club = input('Enter your club: ')
      soccer_data[your_city] = [your_club]

with open('list-tuple/pys.json', 'w') as file:
      json.dump(soccer_data, file, indent=2)

