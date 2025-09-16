
import random
class person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value


p1 = person("홍길동", 20)
print(p1.age)
p1.age = 30
print(p1.age)