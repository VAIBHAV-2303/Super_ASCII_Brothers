'''

[MM]
 ][

This file contains the Mario class
which generates mario itself and its
movement function '''

from person import Person

class Mario(Person):

    '''Mario class'''

    def __init__(self):
        '''Initialization'''
        Person.__init__(self)
        self.lives = 3
        self.posx = 20
        self.posy = 20
        self.inair = False
        self.inairtime = None
        self.bulletarr = []
        self.superpower = False

    def shoot(self):
        '''Shooting function'''
        self.bulletarr.append([self.posx, self.posy])

    def supershoot(self):
        '''Special power shoot'''
        self.bulletarr.append([self.posx, self.posy])
        self.bulletarr.append([self.posx - 1, self.posy])
        self.bulletarr.append([self.posx + 1, self.posy])

    def lose(self, Globalvar, Enemyarr, brickarr, coinarr, springarr, pipearr):
        '''Loosing life'''
        self.inair = False
        self.lives -= 1
        Enemyarr.clear()
        for _ in range(10):
            self.move('a', Globalvar, Enemyarr, brickarr,
                      coinarr, springarr, pipearr)

        self.posx = 20
        self.posy = 20

        # Corrected Code
        if Globalvar.waterx <= 20 and Globalvar.waterx + 15 >= 20:
            for _ in range(10):
                self.move('a', Globalvar, Enemyarr, brickarr,
                          coinarr, springarr, pipearr)
        self.posx = 20
        self.posy = 20

    def bossmove(self, character, Boss):
        '''Movement during boss round'''
        if character == 'a':
            if self.posy > 1:
                self.posy -= 1
        elif character == 'd':
            if self.posy < Boss.posY - 10:
                self.posy += 1
        elif character == 'w':
            if not self.inair:
                self.inair = True
                self.posx -= 1
                self.inairtime = 1

        if self.inair:
            self.inairtime += 1
            if self.inairtime == 3:
                self.posx -= 1
            if self.inairtime == 7:
                self.posx -= 1
            if self.inairtime == 12:
                self.posx -= 1
            if self.inairtime == 17:
                self.posx += 1
            if self.inairtime >= 20:
                self.posx += 1

    def Superjump(self):
        '''Spring jump'''
        self.inair = True
        self.posx -= 4
        self.inairtime = 1
