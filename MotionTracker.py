#------------------------------------------(Motion Tracker)----------------------------------------------

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
#------------------------------------------(the real stuff)---------------------------------------------------



class Player():
    def __init__(self):
        self.mt = MotionTracker()
        self.hp = 10
        self.healpot = 2
        self._poison = False
        
    def health(self):
        return self.hp
    
    def take_damage(self, damage):
        self.hp -= damage
        
    def heal(self):
        if self.healpot >= 1:
            self.healpot -= 1
            self.hp = 10
            print('''✔
    
---''')
        else:
            print('''ur out of heal pots.
this is why you don't spam heal your level 6 bulbasaur smh
---
''')
    def poison(self):
        self._poison = True

    def status(self):
        if self._poison:
            self.take_damage(1)
    
    def stats(self, damage_taken):
        print('health:',  health())
        print('damage taken:', damage_taken)

#------------------------------------------(Game)--------------------------------------------------------------
class Game():
    def __init__(self):
        self.gu_mine = {(-1, -1)}
    #------------------------------------------(process_command)-----------------------------------------------
    def process_command(self, mt, command):
        play = Player()
        # go forward, turn left, turn right, location
        if command == 'go forward':
            mt.move()
            return '''✔
        
---'''
        if command == 'turn left':
            mt.turn_left()
            return '''✔


---'''
        if command == 'turn right':
            mt.turn_right()
            return '''✔

---'''
        if command == 'location':
            return('({}, {})'.format(mt.get_x(), mt.get_y()))

        if command == 'turn around':
            mt.turn_right()
            mt.turn_right()
            return '''✔

---'''
        if command == 'freemove':
            cmd_selfmove()
            return '''✔

---'''
                    
        if command == 'heal':
            play.heal()
                
        if command == 'stats':
            print('health:', play.health())
            print('location: ({}, {})'.format(mt.get_x(), mt.get_y()))

        if command == 'inputs':
            print(''' [go forward, turn right, turn left, turn around, location, freemove, heal, stats, input(current)]
''')
        else:
            play.movement()
            return 'you tripped and fell'

    #------------------------------------------(playgame)-------------------------------------------------------
    def playgame(self):
        play = Player()
        while True: 
            if play.mt.get_x() == 1 and play.mt.get_y() == 1:
                play.take_damage(damage_taken)
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

            play.status()
            
            command = input("What dyou wanna do?\n => ")
            result = self.process_command(play.mt, command)
            print(result)
