'''Contains The Person Class
    which is the parent class for 
    mario and enemies'''


class person():

    def __init__(self):
        '''Initialization'''
        self.lives = None
        self.posX = None
        self.posY = None
        self.inair = False
        self.inairtime = None

    def move(self, character, Globalvar, Enemyarr, Brickarr, Coinarr, springarr, Pipearr):
        '''Core movement function'''

        '''gravity effect'''
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

        if character == 'a':
            Globalvar.update('a', Enemyarr, Brickarr,
                             Coinarr, springarr, Pipearr)
        elif character == 'd':
            Globalvar.update('d', Enemyarr, Brickarr,
                             Coinarr, springarr, Pipearr)
        elif character == 'w':
            if self.inair == False:
                self.inair = True
                self.posX -= 1
                self.inairtime = 1
