class KoreanCollege:
      def __init__(self, name, year):
            self.name = name
            self.year = year
      def __repr__(self):
            return f'{type(self).__name__}(University name: {self.name}; Founded year: {self.year})'

sogang = KoreanCollege('Sogang', 1960)
print(sogang)