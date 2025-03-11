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
            super().recruite(self)
      
class Meta(Job):
      def __init__(self, company, position, salary, remote, holiday):
            super().__init__(company, position, salary)
            self.remote = remote
            self.holiday = holiday
      def recruite(self):
            return f'{super().recruite()}. You can work {self.remote} regime. You can have {self.holiday} days of annual holiday'

google = Google('Google', 'Manager', 160000, 'hybrid (in-office and remote)')
meta = Meta('Meta', 'Machine Learning Engineer', 220000, 'hybrid (in-office and remote)', 30)

print(google.recruite())
print(meta.recruite())