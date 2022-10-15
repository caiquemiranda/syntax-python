"""
syntax template class

class ClassName(object):
    'Class'

    class_variable = 'x'

    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return  'object as a string'

    def other_method(self, *args):
        pass


syntax template super class

class ClassName(SuperClass):
    # same as above
    # use 'super' keyword to get from above

"""


class Horse(object):

    species = 'Equus ferus caballus'

    def __init__(self, color, weight, wild=False):
        self.color = color
        self.weight = weight
        self.wild = wild

    def __repr__(self):
        return f'{self.color} horse weight {self.weight} and wild status is {self.wild}'

    def make_sound(self):
        print('Sound of horse')

    def movement(self):
        return 'walk'


class RaceHouse(Horse):
    'A fest Horse'

    def movement(self):
        return 'rum'

    def movement_slow(self):
        return super().movement()

    def __repr__(self):
        return f'{self.color} race house weighing {self.weight} and wild status is {self.wild}'


horse = RaceHouse('White', 200)

print(horse.movement())
print(horse.movement_slow())
