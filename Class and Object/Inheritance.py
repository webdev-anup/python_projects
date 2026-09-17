class Person:
    def __init__(self, first_name, last_name, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.first_name} {self.last_name}, {self.age}, {self.country}, {self.city}'

    def add_skill(self, skill):
        self.skills.append(skill)


class Student(Person):
    pass


s1 = Student('Anup', 'Patwa', 20, 'India', 'Mumbai')
s2 = Student('John', 'Doe', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
