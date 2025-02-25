soccer_teams = {
      "Milan": ['Inter Milan', 'Milan'],
      "London": ['Arsenal', 'Chelsea', 'Tottenham Hotspur', 'West Ham', 'Crystal Palace'],
      'Madrid': ['Atletico Madrid', 'Getafe CF', 'CD Leganes', 'Rayo Vallecano', 'Real Madrid'],
      "Barcelona": ['Barcelona', 'Espanyol'],
      "Turin": ['Juventus', 'Torino'],
      
}

your_city = input('Enter your city name: ')
your_club = input('Enter your club: ')

for city, club in soccer_teams.items():
      if your_city == city:
            club.append(your_club)
            print(soccer_teams)
            break
else:
      soccer_teams[your_city] = [your_club]
      print(soccer_teams)

