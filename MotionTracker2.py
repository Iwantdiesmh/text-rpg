#------------------------------------------(Motion Tracker)---------------------------------------------------

class MotionTracker:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'north'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction 

    def turn_left(self):
        if self.direction == 'north':
            self.direction = 'west'
        elif self.direction == 'west':
            self.direction = 'south'
        elif self.direction == 'south':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'north'
    def turn_right(self):
        if self.direction == 'north':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'south'
        elif self.direction == 'south':
            self.direction = 'west'
        elif self.direction == 'west':
            self.direction = 'north'
            
    def move(self, distance = 1):
        if self.direction == 'north':
            self.y += distance
        elif self.direction == 'west':
            self.x -= distance
        elif self.direction == 'south':
            self.y -= distance
        elif self.direction == 'east':
            self.x += distance
#------------------------------------------(the real stuff)------------------------------------------------------

class Player():
    def __init__(self):
        self.mt = MotionTracker()
        self.hp = 10
        self.healpot = 2
        self._poison = False
        self.currency = 1000
        self.casual = True
        self.shop = False
        
    def health(self):
        return self.hp
    
    def take_damage(self, damage):
        self.hp -= damage
        
    def heal(self):
        if self.healpot >= 1:
            self.healpot -= 1
            self.hp = 10
            print('done')
        else:
            print('''ur out of heal pots.
this is why you don't spam heal your level 6 bulbasaur smh
''')
            
    def poison(self):
        self._poison = True

    def unpoison(self):
        self._poison = False

    def remove_gu_mine(self):
        self._poison = False
        
    def status(self):
        if self._poison:
            self.take_damage(1)
            print('*poison damage*')
    
    def stats(self, damage_taken):
        print('health:',  self.health())
        print('damage taken:', damage_taken)
        
    def c_healthpot(self):
        self.healpot += 1

    def currency(self):
        return self.currency()

    def currency_change(self, amount):
        self.currency += amount

    def mode_casual(self):
        self.casual = True
        self.shop = False

    def mode_shop(self):
        self.casual = False
        self.shop = True

    def casual(self):
        return self.casual

    def shop(self):
        return self.shop

    def s_healpots(self):
        if self.currency >= 200:
            self.healpot += 1
            
#------------------------------------------(Game)---------------------------------------------------------------
class Game():
    def __init__(self):
        self.gu_mine = {(-1, -1), (4, 2)}
    #------------------------------------------(process_command)-----------------------------------------------
    def process_command(self, p, command):
        check =  '''✔
        
---'''
        
        if command == 'go forward':
            p.mt.move()
            p.status()
            return check

        if command == 'turn left':
            p.mt.turn_left()
            p.status()
            return check

        if command == 'turn right':
            p.mt.turn_right()
            p.status()
            return check

        if command == 'turn around':
            p.mt.turn_right()
            p.mt.turn_right()
            p.status()
            return check

        if command == 'heal':
            p.heal()
            return check

        if command == 'stats':
            return 'health: {}\nlocation: ({}, {})\ncredits: {}'.format(p.health(), p.mt.get_x(), p.mt.get_y(), p.currency)

        if command == 'inputs':
            return (''' [go forward, turn right, turn left, turn around, location, free move(doesn't work), heal, stats, F (pull out gu mines), shop (doesn't work), input(current)]
''')
        if command == 'iwantdie':
            return ("wow ok (ya suck)")

        if command == 'shop':
            p.mode_shop()
            return check
            
        if command == 'F':
            p.unpoison()
            return check
        
        else:
            p.status()
            return 'you tripped and fell'

    def process_command_shop(self, p, buy):
        if buy == 'health pot':
            p.s_healpots()

        if buy == 'leave':
            p.mode_casual()
    #------------------------------------------(playgame)--------------------------------------------------------
    def playgame(self):
        play = Player()
        while play.casual == True: 
            if play.mt.get_x() == 1 and play.mt.get_y() == 1:
                play.take_damage(2)
                play.stats(2)

            position = (play.mt.get_x(), play.mt.get_y())
            if position in self.gu_mine:
                print('you stepped on a gu mine! Oh no too bad youll be taking damage of 1 each step')
                play.poison()

            if play.health() == 0:
                print('''---
    game over (ya suck)
    ---''')
                break
            
            command = input("What dyou wanna do?\n => ")
            result = self.process_command(play, command)
            print(result)
            
        while play.shop == True:
            buy = input("What do you want to buy\n => ")
            s_result = self.process_command_shop(play, command)
            print(result)

game = Game()
game.playgame()
casual = True

#potential ideas that make me want die
#currency ✔
#actual poison lmao ✔
#graphics
#upgrades

#--- so I added a shop. It works, but I cant exit it. Weird, it uses the same come to enter the shop. smh
