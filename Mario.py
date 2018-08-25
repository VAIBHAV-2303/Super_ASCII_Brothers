''' 

[MM]
 ][

'''


''' This file contains the Mario class 
    which generates mario itself and its 
    movement function  '''

from Person import person


class mario(person):

    def __init__(self):
        '''Initialization'''
        person.__init__(self)
        self.lives = 3
        self.posX = 20
        self.posY = 20
        self.inair = False
        self.inairtime = None
        self.bulletarr = []
        self.superpower = False

    def shoot(self):

        self.bulletarr.append([self.posX, self.posY])

    def supershoot(self):

        self.bulletarr.append([self.posX, self.posY])
        self.bulletarr.append([self.posX - 1, self.posY])
        self.bulletarr.append([self.posX + 1, self.posY])

    def lose(self, Globalvar, Enemyarr, Brickarr, Coinarr, springarr, Pipearr):
        '''Losing life'''
        self.inair = False
        self.lives -= 1
        Enemyarr.clear()
        for _ in range(10):
            self.move('a', Globalvar, Enemyarr, Brickarr,
                      Coinarr, springarr, Pipearr)
        self.posX = 20
        self.posY = 20

    def bossmove(self, character, Boss):
        '''Movement during boss round'''
        if character == 'a':
            if self.posY > 1:
                self.posY -= 1
        elif character == 'd':
            if self.posY < Boss.posY - 10:
                self.posY += 1
        elif character == 'w':
            if self.inair == False:
                self.inair = True
                self.posX -= 1
                self.inairtime = 1

        if self.inair == True:
            self.inairtime += 1
            if self.inairtime == 3:
                self.posX -= 1
            if self.inairtime == 7:
                self.posX -= 1
            if self.inairtime == 12:
                self.posX -= 1
            if self.inairtime == 17:
                self.posX += 1
            if self.inairtime >= 20:
                self.posX += 1

    def Superjump(self):
        '''Spring jump'''
        self.inair = True
        self.posX -= 4
        self.inairtime = 1
