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

    def move(self):
        if self.direction == 'north':
            self.y += 1
        elif self.direction == 'west':
            self.x -= 1
        elif self.direction == 'south':
            self.y -= 1
        elif self.direction == 'east':
            self.x += 1
            
    def selfmove(self, distance):
        if self.direction == 'north':
            self.y += distance
        elif self.direction == 'west':
            self.x -= distance
        elif self.direction == 'south':
            self.y -= distance
        elif self.direction == 'east':
            self.x += distance
#------------------------------------------(the real stuff)---------------------------------------------------

def playgame():
    play = Player()
    while True:
        
        if play.mt.get_x() == 1 and play.mt.get_y() == 1:
            play.take_damage(damage_taken)
            play.stats(2)
            
        if play.mt.get_x() == -1 and play.mt.get_y() == -1:
            play.poison2 = True
            print('you stepped on a gu mine! Oh no too bad youll be taking damage of 2 each step owo')
            
        if play.health() == 0:
            print('''---
game over (ya suck)
---''')
            break

        command = input("What dyou wanna do?\n => ")
        result = process_command(play.mt, command)
        print(result)

        
#------------------------------------------(class Player [play])----------------------------------------------------

class Player():
    def __init__(self):
        self.mt = MotionTracker()
        self.hp = 10
        self.healpot = 2
        self.poison2 = False
        self.action = False
        
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
        if poison2 == True:
            if action == True:
                self.hp -= 2
                stats()

    def stats(damage_taken):
        print('health:',  health())
        print('damage taken:', damage_taken)

    def movement():
        self.action = True
        self.action = False

#------------------------------------------(Process_command)----------------------------------------------

def process_command(mt, command):
    play = Player()
    # go forward, turn left, turn right, location
    if command == 'go forward':
        mt.move()
        play.movement()
        return '''✔
        
---'''
    if command == 'turn left':
        mt.turn_left()
        play.movement()
        return '''✔


---'''
    if command == 'turn right':
        mt.turn_right()
        play.movement()
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

#------------------------------------------(Eh)--------------------------------------------------------------

def cmd_selfmove():
    play = Player()
    play.selfmove(int(input("Steps => ")))
