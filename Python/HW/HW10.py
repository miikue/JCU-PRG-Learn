

class Warrior():
    def __init__(self, health=50, is_alive=True):
        self.health = health
        self.is_alive = is_alive
        self.attack = 5

class Knight(Warrior):
    def __init__(self, health=50, is_alive=True):
        super().__init__(health, is_alive)
        self.attack = 7

class Defender(Warrior):
    def __init__(self, health=50, is_alive=True):
        super().__init__(health*1.5, is_alive)
        self.attack = 3

class Mage(Warrior):
    def __init__(self, health=50, is_alive=True):
        super().__init__(health*0.7, is_alive)
        self.attack = 10


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False
        
def fancy_fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        print(f"{unit_1.__class__.__name__} attacks {unit_2.__class__.__name__} for {unit_1.attack} damage")
        if unit_2.health <= 0:
            unit_2.is_alive = False
            print(f"{unit_2.__class__.__name__} is dead")
            return True
        unit_1.health -= unit_2.attack
        print(f"{unit_2.__class__.__name__} attacks {unit_1.__class__.__name__} for {unit_2.attack} damage")
        if unit_1.health <= 0:
            unit_1.is_alive = False
            print(f"{unit_1.__class__.__name__} is dead")
            return False

def test():

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False

    miiku = Mage()
    foxtrot = Defender()

    assert fancy_fight(miiku, foxtrot) == True

    print("All tests passed")


test()