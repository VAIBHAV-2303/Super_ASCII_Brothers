'''Contains The Person Class
    which is the parent class for
    mario and enemies'''


class Person():
    '''Person Class'''
    def __init__(self):
        '''Initialization'''
        self.lives = None
        self.posx = 0
        self.posy = None
        self.inair = False
        self.inairtime = None

    def move(self, character, globalvar, enemyarr, brickarr, coinarr, springarr, pipearr):
        '''Core movement function'''

        # gravity effect
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

        if character == 'a':
            globalvar.update('a', enemyarr, brickarr,
                             coinarr, springarr, pipearr)
        elif character == 'd':
            globalvar.update('d', enemyarr, brickarr,
                             coinarr, springarr, pipearr)
        elif character == 'w':
            if not self.inair:
                self.inair = True
                self.posx -= 1
                self.inairtime = 1
