class Character:    
    """ Base character class for MINI RPG """
    _hp_per_level = 10
    def __init__(self, name, race="Human", level=1):
        self.name = name
        self.race = race
        self.level = level
        self.hp = self._hp_per_level * self.level

    def attack(self):
        raise NotImplementedError()

    def move(self, direction):
        """ Update location based on direction argumnent."""
        if direction == 'north':
            self.location = (self.location[0] - 1, self.location[1])
        elif direction == 'south':
            self.location = (self.location[0] + 1, self.location[1])
        elif direction == 'west':
            self.location = (self.location[0], self.location[1] - 1)
        elif direction == 'east':
            self.location = (self.location[0], self.location[1] + 1)
        else:
            raise ValueError('Unknown direction: ' + str(direction))

class Wizard(Character):
    """ Wizard Rule !! """
    def __init__(self, name, race="Elf", level=1):
        self._hp_per_level = 5
        super(self).__init__(name, race, level)
    
    def attack(self):
        print('In the name of Bael I cast, tripple fire blast!')

    def teleport(self, location):
        self.location = location
        