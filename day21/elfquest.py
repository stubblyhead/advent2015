class Character:
    def __init__(self, hp, dmg, ac):
        self.hp = hp
        self.dmg = dmg
        self.ac = ac

    def get_ac(self):
        return self.ac
    
    def get_hp(self):
        return self.ac
    
    def get_dmg(self):
        return self.dmg
    
    def take_damage(self, amt):
        actual = max([1,amt-self.ac])
        self.hp -= actual

    def get_item(self, item):
        self.ac += item.ac
        self.dmg += item.dmg

class Item:
    def __init__(self, cost, dmg, ac):
        self.cost = cost
        self.dmg = dmg
        self.ac = ac


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

