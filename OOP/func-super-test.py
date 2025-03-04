class Job:
      def __init__(self, company, position, salary):
            self.company = company
            self.position = position
            self.salary = salary
      def recruite(self):
            return f'{self.company}: We are hiring {self.position} with {self.salary:,}$ salary a year'
class Google(Job):
      def __init__(self, company, position, salary):
            super().__init__(company, position, salary)
      def recruite(self):
            return super().recruite()
      
class Meta(Job):
      def __init__(self, company, position, salary):
            super().__init__(company, position, salary)
      def recruite(self):
            return super().recruite()

google = Google('Google', 'Manager', 160000)
meta = Meta('Meta', 'Machine Learning Engineer', 220000)

print(google.recruite())
print(meta.recruite())