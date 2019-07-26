import random


class Stats():
    def __init__(self, atk, defe, spe, maxhp):
        self.atk = atk
        self.defe = defe
        self.spe = spe
        self.maxhp = maxhp

class Pokémon():
    def __init__(self, stats, name, typee, moves):
        self.name = name
        self.typee = typee
        self.stats = stats
        self.hp = stats.maxhp
        self.moves = moves

    def tackle(self, target):
        target.take_damage(self.damage(target, 40))

    def damage(self, target, power):
        dmg = (self.stats.atk * power)//(target.stats.defe * 10)
        return dmg

    def growl(self, target):
        target.stats.atk = target.stats.atk * 2 // 3

    def shell_smash(self):
        self.stats.atk *= 2
        self.stats.spe *= 2
        self.stats.defe = self.stats.defe * 2 // 3
        

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        print('{} has {} hp'.format(self.name, self.hp))
            
    def do_move(self, target, choice):
        move = self.moves[choice]
        print('{} used {}!'.format(self.name, move))
        if move == 'tackle':
            self.tackle(target)
        if move == 'growl':
            self.growl(target)
        if move == 'shell_smash':
            self.shell_smash()
P = Pokémon
def makePidgey():
    stats = Stats(12, 10, 12, 20)
    pidgey = P(stats, 'ur mom', 'Flying, Dragon', ['tackle', 'shell_smash'])
    return pidgey

def makeZigzagoon():
    stats = Stats(7, 8, 9, 16)
    zigzagoon = P(stats, 'ZIGGY', 'Ground, Rock', ['tackle', 'growl'])
    return zigzagoon

def playgame():
    p = makePidgey()
    z = makeZigzagoon()
    while p.hp > 0 and z.hp > 0:
        a = int(input('wut u want do 0(tackle) or 1(shell smash)'))
        p.do_move(z, a)
        if z.hp > 0:
            choice = random.randint(0,len(z.moves)-1)
            z.do_move(p, choice)
    if z.hp == 0:
        return 'zig ded'
    else:
        return 'pid ded'
        
