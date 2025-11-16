from itertools import combinations

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
    boss_ac = int(lines[2].split(': ')[1])
    weapons = {}
    armor = {}
    rings = {}
    
    with open('weapons') as f:
        lines = f.readlines()
    for l in lines:
        name, cost, dmg, ac = l.split()
        weapons[name] = Item(int(cost),int(dmg),int(ac))

    with open('armor') as f:
        lines = f.readlines()
    for l in lines:
        name, cost, dmg, ac = l.split()
        armor[name] = Item(int(cost),int(dmg),int(ac))

    with open('rings') as f:
        lines = f.readlines()
    for l in lines:
        name, cost, dmg, ac = l.split()
        rings[name] = Item(int(cost),int(dmg),int(ac))


    
    min_cost = 356

    for w in weapons.values():
        for a in armor.values():
            for r in rings.values():
                boss = Character(boss_hp, boss_dmg, boss_ac)
                this_cost = w.cost + a.cost + r.cost
                player = Character(100,0,0)
                for x in [w,a,r]:
                    player.get_item(x)
                if fight(player, boss) == 'player':
                    min_cost = min([min_cost, this_cost])
            for c in combinations(rings.values(),2):
                boss = Character(boss_hp, boss_dmg, boss_ac)
                this_cost = w.cost + a.cost
                player = Character(100,0,0)
                for r in c:
                    this_cost += r.cost
                for x in [w,a]+list(c):
                    player.get_item(x)
                if fight(player,boss) == 'player':
                    min_cost = min([min_cost, this_cost])
    print(min_cost)
                

    