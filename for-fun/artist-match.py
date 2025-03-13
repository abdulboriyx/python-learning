# class ArtistMatch:
#       def __init__(self, data):
#             self.data = {}

#       def __setitem__(self, key, value):
#             self.data[key] = value

#       def __getitem__(self, index):
#             return self.data[index]
      




mine_artist = [
      {
            "name": "Kendrick Lamar",
            "genre": "Hip-Hop"
      }, {
            "name": "Jay Z",
            "genre": "Hip-Hop"
      }, {
            "name": "Beyonce",
            "genre": "Country"
      }, {
            "name": "Taylor Swift",
            "genre": "Pop"
      }, {
            "name": "Dua Lipa",
            "genre": "Pop"
      }, {
            "name": "Lady Gaga",
            "genre": "Pop"
      }, {
            "name": "Kanye West",
            "genre": "Hip-Hop"
      }, {
            "name": "Queen",
            "genre": "Rock"
      }, {
            "name": "Pink Floyd",
            "genre": "Rock"
      }, {
            "name": "Childish Gambino",
            "genre": "Hip-Hop"
      }
]

your_artist = [
      {
            "name": "Kendrick Lamar",
            "genre": "Hip-Hop"
      }, {
            "name": "Future",
            "genre": "Hip-Hop"
      }, {
            "name": "Adele",
            "genre": "Country"
      }, {
            "name": "The Weeknd",
            "genre": "Pop"
      }, {
            "name": "Childish Gambino",
            "genre": "Hip-Hop"
      }, {
            "name": "Kanye West",
            "genre": "Hip-Hop"
      }, {
            "name": "Dua Lipa",
            "genre": "Pop"
      }
]

matched_artists = []
unmatched_artists = []
def get_artist():
      for my_artist in mine_artist:
            if my_artist in your_artist:
                  matched_artists.append(my_artist["name"])
            else:
                  unmatched_artists.append(my_artist["name"])

get_artist()
print(f"These are common artists:", ", ".join(matched_artists))
print(f'These are unshared artists:', ", ".join(unmatched_artists))