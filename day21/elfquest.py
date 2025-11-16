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

def fight(player, boss):
    while True:
        boss.take_damage(player.dmg)
        if boss.hp <= 0:
            return "player"
        player.take_damage(boss.dmg)
        if player.hp <= 0:
            return "boss"

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
        boss_hp = int(lines[0].split(': ')[1])
        boss_dmg = int(lines[1].split(': ')[1])
        boss_ac = int(lines[1].split(': ')[1])
        # boss = Character(boss_hp, boss_dmg, boss_ac)
        boss = Character(12,7,2)      
        player = Character(8,5,5)

        print(fight(player, boss))