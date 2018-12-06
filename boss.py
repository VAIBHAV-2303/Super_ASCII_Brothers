'''

()
||
/\

Contains the boss class'''


class Boss():
    '''Boss class'''
    def __init__(self):
        '''Initialization'''
        self.posX = 19
        self.inair = False
        self.posY = 89
        self.hurt = 0
        self.bulletarr = []
        self.health = 5

    def moveleft(self):
        '''Left movement'''
        if self.posY > 2:
            self.posY -= 1

    def moveright(self):
        '''Right movement'''
        if self.posY < 78:
            self.posY += 1

    def always(self):
        '''Inair handling'''
        if self.inair:
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

    def movejump(self):
        '''Jump movement'''
        if not self.inair:
            self.inair = True
            self.posX -= 1
            self.inairtime = 1

    def shoot(self):
        '''Random continuous shooting'''
        self.bulletarr.append([self.posX + 1, self.posY])
