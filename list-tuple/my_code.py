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
except:
#     soccer_data = [] -> I started as a list while it should be dict
      soccer_data = {}
# here I overwrote the json file whether it had new entries or not 
with open('list-tuple/pys.json', 'w') as file:
    json.dump(soccer_teams, file, indent=2)

your_city = input('Enter your city name: ')

for city, club in soccer_data.items():
    if your_city in city:
        your_club = input('Enter your club: ')
        soccer_teams[city].append(your_club)

with open('list-tuple/pys.json', 'w') as file:
    json.dump(soccer_teams, file, indent=2)
