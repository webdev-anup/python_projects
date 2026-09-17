class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Anup', 'Patwa', 20, 'India', 'Mumbai')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)