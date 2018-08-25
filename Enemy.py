'''

/\
oo

'''


'''This file contains the enemy class 
	which inherits from person class'''

from Person import person


class enemy(person):

    def __init__(self):

        person.__init__(self)
        self.lives = 1
        self.posX = 21
        self.posY = 89
        self.inair = False
        self.inairtime = None
        self.dir = 1

    '''Polymorphism'''

    def move(self):

        self.posY -= self.dir

        '''gravity effect'''
        if self.inair == True:
            self.inairtime += 1
            if self.inairtime == 5:
                self.posX -= 1
            if self.inairtime == 11:
                self.posX -= 1
            if self.inairtime == 14:
                self.posX += 1
            if self.inairtime == 17:
                self.posX += 1
            if self.inairtime >= 20:
                self.posX += 1
