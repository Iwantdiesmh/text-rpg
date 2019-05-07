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

    def turn_around(self):
        self.turn_right()
        self.turn_right()

def process_command(mt, command):
    if command == 'go forward':
        mt.move()
        return 'done'
    elif command == 'turn right':
        mt.turn_right()
        return 'done'
    elif command == 'turn left':
        mt.turn_left()
        return 'done'
    elif command == 'turn around':
        mt.turn_around()
        return 'done'
    elif command == 'where am I?':
        return '({}, {})'.format(mt.get_x(), mt.get_y())
    else:
        return 'Are you dumb'

def play_game():
    p = Player()
    while True:
        command = input("What do you want to do?\n> ")
        result = process_command(p.compass, command)
        print(result)
        if p.compass.get_x() == 1 and p.compass.get_y() == 1:
            p.damage_square()
            print('Minus 2 health. You have', p.health, 'health left')
            if p.dead():
                print('You died')
            break
        elif p.compass.get_x() == -1 and p.compass.get_y() == -1:

            print('fine u found the real easter egg u can keep going')

class Player:
    def __init__(self):
        self.compass = MotionTracker()
        self.health = 10
    def take_damage(self, damage):
        self.health -= damage
    def damage_square(self):
        self.health -= 2
    def dead(self):
        return self.health <= 0

            
        
