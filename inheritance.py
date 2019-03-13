# -*- coding: utf-8 -*-

class Pet(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<{__class__.__name__}: {name}>'.format(__class__ = self.__class__, **self.__dict__)


class Dog(Pet):

    pass


class Cat(Pet):

    pass


cat = Cat('flok')
dog = Dog('rex');

print(cat)
print(dog)
