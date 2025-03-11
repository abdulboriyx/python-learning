# friendly-user

class University:
      def __init__(self, name, city):
            self.name = name
            self.city = city

      def __str__(self):
            return f'{self.name} is located in {self.city}'
class UCL(University):
      def __init__(self, name, city, major, professor, offcampus):
            super().__init__(name, city)
            self.major = major
            self.professor = professor
            self.offcampus = offcampus
      def __str__(self):
            return f'{self.name} is located in {self.city}. {self.major} is leading major of the college. {self.professor} is the leading professor in UCL. {self.offcampus} is the advantage of off-campus live.'
class UCLA(UCL):
      def __init__(self, name, city, major, professor, offcampus, weather):
            super().__init__(name, city, major, professor, offcampus)
            self.weather = weather
      def __str__(self):
            return f'{self.name} is located in {self.city}. {self.major} is leading major of the college. {self.professor} is the leading professor in UCL. {self.offcampus} is the advantage of off-campus live. {self.weather} is a big  advantage compared to UCL' 
class MIT(UCLA):
      def __init__(self, name, city, major, professor, offcampus, weather, finance):
            super().__init__(name, city, major, professor, offcampus, weather)
            self.finance = finance
      def __str__(self):
            return f'{self.name} is located in {self.city}. {self.major} is leading major of the college. {self.professor} is the leading professor in UCL. {self.offcampus} is the advantage of off-campus live. {self.weather} is a bit harsh. {self.finance} is a real advantage.'


ucl = UCL('University College London', 'London', 'Neuroscience', 'Baroness Susan Greenfield', 'Silicon Roundabout')
ucla = UCLA('University of California, Los Angeles', 'Los Angeles', 'Film and Television', 'Frances Arnold', 'Hollywood', 'Warm Weather')
mit = MIT('MIT', 'Massachusetts', 'Computer Science & AI', 'John McCarthy', 'Cold weather', 'Boston’s Kendall Square', 'Financing startups')

print(f'{ucl}\n')
print(f'{ucla}\n')
print(f'{mit}\n')