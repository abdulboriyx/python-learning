class ArtistMatch:
      def __init__(self, name):
            self.name = name
      def __eq__(self, other):
            if isinstance(other, ArtistMatch):
                  return self.name == other.name
            else:
                  raise TypeError('Error!')

myartist = ArtistMatch('Kendrick, Future, Tyler')
yourartist = ArtistMatch('Kendrick, Future, ASAP')

print(myartist == yourartist)