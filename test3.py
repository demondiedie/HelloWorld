"""import math
print(dir(math))
#print(math.sqrt(4))

from math import ceil,floor
print(ceil(3.7))
print(floor(3.7))
"""


class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0


    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo....yo...microphone check.....'

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


if __name__ == '__main__':
    i = Human(name="Ian")
    i.say("hi")
    j = Human("Joel")
    j.say("hello")
    i.say(i.get_species())
    Human.species = "H. Neanderthalensis"
    i.say(i.get_species())
    j.say(j.sing())
    print(Human.grunt())

    i.age = 42
    i.say(i.age)
    j.say(j.age)
    del j.age

    try:
        j.say(j.age)
    except:
        print("harro")

