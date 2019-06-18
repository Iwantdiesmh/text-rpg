
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
        self.healpot = 1
        self.smallheal= 2
        self._poison = False
        self.currency = 1000
        self.casual = True
        self.shop = False
        self.freemove = False
        self.upgrades = False
        self.upgrade_heal = 2
        self.upgrade_max_hp = 10

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

    def healpotamount(self):
        return self.healpot
        
    def currency(self):
        return self.currency()

    def currency_change(self, amount):
        self.currency += amount

    def mode_casual(self):
        self.casual = True
        self.shop = False
        self.freemove = False
        self.upgrades = False

    def mode_shop(self):
        self.casual = False
        self.shop = True
        self.freemove = False
        self.upgrades = False
        
    def mode_freemove(self):
        self.casual = False
        self.shop = False
        self.freemove = True
        self.upgrades = False

    def mode_upgrades(self):
        self.casual = False
        self.shop = False
        self.freemove = False
        self.upgrades = True
    
    def freemove(self):
        return self.freemove
        
    def casual(self):
        return self.casual

    def shop(self):
        
        return self.shop

    def s_healpots(self):
        if self.currency >= 200:
            self.currency -= 200
            self.healpot += 1
        else:
            print('STOP WASTING YOUR MONEY ON YOUR LEVEL 6 BULBASAUR SMH')

    def small_heal(self):
        if self.smallheal >= 1:
            self.smallheal -= 1
            self.health += self.upgrade_heal
            print('''ur out
''')
            
#------------------------------------------(Game)---------------------------------------------------------------
class Game():
    def __init__(self):
        self.gu_mine = {(-1, -1), (4, 2)}
        self.money_mine = {(2, 1), (-2, -3)}
        self.spikes = {(1, 1), (-4, 0)}
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

        if command == 'max heal':
            p.heal()
            return check
        
        if command == 'heal':
            p.small_heal()
            return check
        
        if command == 'freemove':
            p.mode_freemove()
            return check
        
        if command == 'stats':
            return 'health: {}\nlocation: ({}, {})\ncredits: {}\nhealth pots: {}'.format(p.health(), p.mt.get_x(), p.mt.get_y(), p.currency,p.healpotamount())

        if command == 'inputs':
            return (''' [go forward, turn right, turn left, turn around, location, free move, heal, stats, F (pull out gu mines), shop
, input(current)]
''')

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
        check =  '''✔
        
---'''
        
        if buy == 'health pot':
            p.s_healpots()
            return check

        if buy == 'items':
            return('''health pot - 200 credits
-leave-
''')

        if buy == 'upgrade':
            p.mode_upgrades()
        
        if buy == 'leave':
            p.mode_casual()

        
        else:
            return 'I dont understand'

    def process_command_freemove(self, p, command):
        check =  '''✔
        
---'''
        p.mt.move(command)
        p.mode_casual()
        return check

    def process_command_upgrades(self, p, command):
        if command == 'upgrades':
            print('''"heal" - adds two hp to small healpot amount-> 500 units
"maximum hp" -> max hp + 2 = 500 units
---''')
        if command == 'upgrade heal':
            if p.currency >= 500:
                p.currency -= 500
                p.upgrade_heal += 2
                return 'done'
            else:
                return 'ur too poor'
        if command == 'upgrade maximum hp':
            if p.currency >= 500:
                p.currency -= 500
                p.upgrade_max_hp += 2
                return 'done'
            else:
                return 'ur too poor'

        if command == 'leave':
            p.mode_casual()
                
                
            
        

#------------------------------------------(playgame)--------------------------------------------------------
    def playgame(self):
        play = Player()
        while True:
            while play.casual == True: 

                position = (play.mt.get_x(), play.mt.get_y())

                if position in self.spikes:
                    print("Youch")
                    play.take_damage(2)
                    
                if position in self.gu_mine:
                    print('you stepped on a gu mine! Oh no too bad youll be taking damage of 1 each step')
                    play.poison()
                           
                if position in self.money_mine:
                    print("Oh look money owo\nplease dont abuse/grind money smh")
                    play.currency_change(200)
                    
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
                result = self.process_command_shop(play, buy)
                print(result)

            while play.freemove == True:
                command = int(input("How many squares do you want to move forward? (if you put a word it will crash)\n => "))
                result = self.process_command_freemove(play, command)
                print(result)

            while play.upgrades == True:
                command = input("what dyou want to upgrade\n => ")
                result = self.process_command_upgrades(play, command)
                print(result)
                
game = Game()
game.playgame()
casual = True

#potential ideas that make me want die
#currency ✔
#actual poison lmao ✔
#graphics *doesn't exist*
#upgrades ✔

