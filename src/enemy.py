'''

/\
oo

This file contains the enemy class
which inherits from person class'''

from person import Person


class Enemy(Person):
    '''Enemy class'''
    def __init__(self):

        Person.__init__(self)
        self.lives = 1
        self.posx = 21
        self.posy = 89
        self.inair = False
        self.inairtime = None
        self.dir = 1

    # Polymorphism

    def move(self):

        self.posy -= self.dir

        # gravity effect
        if self.inair:
            self.inairtime += 1
            if self.inairtime == 5:
                self.posx -= 1
            if self.inairtime == 11:
                self.posx -= 1
            if self.inairtime == 14:
                self.posx += 1
            if self.inairtime == 17:
                self.posx += 1
            if self.inairtime >= 20:
                self.posx += 1
