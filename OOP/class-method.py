import re
class Hiring:
      def __init__(self, name, age, gender, education, email):
            if not name:
                  raise ValueError('Missing name')
            self.name = name
            self.age_check = age 
            self.gender = gender
            self.edu_bg = education 
            self.email_check = email
      
      @classmethod
      def hire(cls):
            name = input('Enter your name: ')
            age = input('Enter your age: ')
            gender = input('Enter your gender: ')
            education = input('Enter your education background: ')
            email = input('Enter your email: ')
            return cls(name, age, gender, education, email)

      @property 
      def edu_bg(self):
            return self._education
      
      @edu_bg.setter
      def edu_bg(self, education):
            if education != 'Ph.D':
                  raise ValueError('Invalid Education quality! We only hire Ph.D holders. ')
            self._education = education

      @property
      def email_check(self):
            return self._email
      
      @email_check.setter
      def email_check(self, email):
            if not re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                  raise ValueError('Invalid Email address!')
            self._email = email
      
      @property
      def age_check(self):
            return self._age
      
      @age_check.setter
      def age_check(self, age):
            if not re.search(r'^(0|[1-9]\d?|1[01]\d|120)$', age):
                  raise ValueError('Invalid age input!')
            self._age = age

      def __str__(self):
            return f'Candidate info:\n Name: {self.name}\n Age: {self._age}\n Gender: {self.gender}\n Education: {self._education}\n Email: {self._email}'


def main():
      hire = Hiring.hire()
      print(hire)


if __name__ == '__main__':
      main()
