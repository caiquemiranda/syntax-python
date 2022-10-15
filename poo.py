class Animal:
    def __init__(self, animal, name, action):
        self.animal = animal
        self.name = name
        self.action = action


animal1 = Animal('Dog', 'Brian', 'running')
print(f'The {animal1.animal} have a name {animal1.name} and stay {animal1.action}')
