class Candidate:
      age_restiction = 18
      def __init__(self, name, age, education):
            self.name = name
            self.age = age
            self.education = education

      def __str__(self):
            return f'Candidate\'s name: {self.name}\nCandidate\'s age: {self.age}\nCandidate\'s education background: {self.education}'
      def experience(self, years):
            return f'{self.name} has {years} years of experience'




candidate = Candidate('Emily Blunt', 37, 'Bachelors')
candidate_experience = candidate.experience('six')


print(f'{candidate}. {candidate_experience}')