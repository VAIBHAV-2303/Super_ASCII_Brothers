'''

   |
   |
   |
30 |               Board      /\
   |                         /  \
   |XXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   |XXXXXXXXXXXX~~~XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   					90

'''

''' This file contains the class
	Board which contains and manages
	the background board scenery '''


import os
from Enemy import enemy
from Brick import brick
from Coin import coin
from Boss import boss
from random import *
from Spring import spring
from Pipe import pipe

'''Locations to spawn enemies'''
'''If mario keeps standing in these positions infinitely many enemies will be spawned'''
EnemyCheckpoints = [
    60, 82, 87,
    170, 173, 175
]

Boss = boss()


class board():

    def __init__(self):
        '''Initialization'''
        self.over = False
        self.height = 30
        self.width = 90
        self.score = 0
        self.coins = 0
        self.layout = []
        self.Enemyarr = []

        self.Pipearr = [
            pipe(18, 315), pipe(18, 60),
            pipe(18, 120), pipe(18, 165)
        ]

        self.springarr = [
            spring(19, 337), spring(19, 390)
        ]

        self.Brickarr = [
            brick("unbreakable", 18, 37), brick(
                "breakable", 18, 40),
            brick("unbreakable", 18, 43), brick(
                "breakable", 14, 40),
            brick("breakable", 18, 113), brick(
                "unbreakable", 14, 121),
            brick("unbreakable", 10, 129), brick(
                "unbreakable", 18, 235),
            brick("unbreakable", 18, 225), brick(
                "unbreakable", 18, 245),
            brick("unbreakable", 14, 230), brick(
                "unbreakable", 14, 240),
            brick("breakable", 10, 235), brick(
                "breakable", 10, 135),
            brick("unbreakable", 14, 143), brick(
                "unbreakable", 18, 151),
            brick("unbreakable", 21, 340), brick(
                "unbreakable", 13, 340),
            brick("unbreakable", 20, 340), brick(
                "unbreakable", 19, 340),
            brick("unbreakable", 18, 340), brick(
                "unbreakable", 17, 340),
            brick("unbreakable", 16, 340), brick(
                "unbreakable", 15, 340),
            brick("unbreakable", 14, 340)
        ]

        self.Coinarr = [
            coin(21, 39), coin(21, 41), coin(21, 43), coin(13, 40),
            coin(9, 129), coin(9, 235), coin(13, 230), coin(13, 240),
            coin(17, 235)
        ]

        for _ in range(self.height):
            self.layout.append([])
        for i in range(self.height):
            for j in range(self.width):
                self.layout[i].append(' ')

        '''Fixed Score, lives and coins in the 1st row'''
        self.layout[0][0] = 'S'
        self.layout[0][1] = 'c'
        self.layout[0][2] = 'o'
        self.layout[0][3] = 'r'
        self.layout[0][4] = 'e'
        self.layout[0][5] = ':'
        self.layout[0][40] = 'L'
        self.layout[0][41] = 'i'
        self.layout[0][42] = 'v'
        self.layout[0][43] = 'e'
        self.layout[0][44] = 's'
        self.layout[0][45] = ':'
        self.layout[0][60] = 'C'
        self.layout[0][61] = 'o'
        self.layout[0][62] = 'i'
        self.layout[0][63] = 'n'
        self.layout[0][64] = 's'
        self.layout[0][65] = ':'

    def updatebg(self, Globalvar):
        '''Score increment on forward movement'''
        self.score = max(self.score, Globalvar.GlobalX)

        '''The base'''
        for i in range(1, self.height):
            for j in range(self.width):
                self.layout[i][j] = ' '

        '''Updating The score'''
        self.layout[0][6] = str(self.score)[0]
        if self.score >= 10:
            self.layout[0][7] = str(self.score)[1]
        if self.score >= 100:
            self.layout[0][8] = str(self.score)[2]

        '''Updating number of coins collected'''
        self.layout[0][66] = str(self.coins)[0]
        if self.coins >= 10:
            self.layout[0][67] = str(self.coins)[1]

        '''Adding Ground'''
        for i in range(22, self.height):
            for j in range(self.width):
                self.layout[i][j] = 'X'

        '''Adding Water'''
        if Globalvar.GlobalX < 300:
            for i in range(22, 25):
                for j in range(Globalvar.waterx, Globalvar.waterx + 10):
                    try:
                        self.layout[i][j] = ' '
                    except:
                        pass

            for i in range(25, self.height):
                for j in range(Globalvar.waterx, Globalvar.waterx + 10):
                    try:
                        self.layout[i][j] = '~'
                    except:
                        pass

        '''Adding Mountains'''
        if Globalvar.GlobalX < 395:
            for i in range(5):
                if Globalvar.Mountainx + i > 0 and Globalvar.Mountainx + i < 90:
                    self.layout[21 - i][Globalvar.Mountainx + i] = '/'
                if Globalvar.Mountainx + 10 - i > 0 and Globalvar.Mountainx + 10 - i < 90:
                    self.layout[21 - i][Globalvar.Mountainx + 10 - i] = '\\'

        '''Adding Clouds'''
        if Globalvar.GlobalX < 360:
            '''Cloud1'''
            if Globalvar.cloudx + 1 > 0 and Globalvar.cloudx + 1 < 90:
                self.layout[4][Globalvar.cloudx + 1] = '('
                self.layout[5][Globalvar.cloudx + 1] = '_'
            if Globalvar.cloudx + 2 > 0 and Globalvar.cloudx + 2 < 90:
                self.layout[4][Globalvar.cloudx + 2] = '_'
                self.layout[5][Globalvar.cloudx + 2] = '_'
            if Globalvar.cloudx + 3 > 0 and Globalvar.cloudx + 3 < 90:
                self.layout[4][Globalvar.cloudx + 3] = '_'
                self.layout[5][Globalvar.cloudx + 3] = ')'
            if Globalvar.cloudx + 4 > 0 and Globalvar.cloudx + 4 < 90:
                self.layout[4][Globalvar.cloudx + 4] = ')'
                self.layout[5][Globalvar.cloudx + 4] = '_'
            if Globalvar.cloudx - 1 > 0 and Globalvar.cloudx - 1 < 90:
                self.layout[5][Globalvar.cloudx - 1] = '('
            if Globalvar.cloudx > 0 and Globalvar.cloudx < 90:
                self.layout[5][Globalvar.cloudx] = '_'
            if Globalvar.cloudx + 5 > 0 and Globalvar.cloudx + 5 < 90:
                self.layout[5][Globalvar.cloudx + 5] = '_'
            if Globalvar.cloudx + 6 > 0 and Globalvar.cloudx + 6 < 90:
                self.layout[5][Globalvar.cloudx + 6] = ')'

            '''Cloud2'''
            if Globalvar.cloud2x + 1 > 0 and Globalvar.cloud2x + 1 < 90:
                self.layout[6][Globalvar.cloud2x + 1] = '('
                self.layout[7][Globalvar.cloud2x + 1] = '_'
            if Globalvar.cloud2x + 2 > 0 and Globalvar.cloud2x + 2 < 90:
                self.layout[6][Globalvar.cloud2x + 2] = '_'
                self.layout[7][Globalvar.cloud2x + 2] = '_'
            if Globalvar.cloud2x + 3 > 0 and Globalvar.cloud2x + 3 < 90:
                self.layout[6][Globalvar.cloud2x + 3] = '_'
                self.layout[7][Globalvar.cloud2x + 3] = ')'
            if Globalvar.cloud2x + 4 > 0 and Globalvar.cloud2x + 4 < 90:
                self.layout[6][Globalvar.cloud2x + 4] = ')'
                self.layout[7][Globalvar.cloud2x + 4] = '_'
            if Globalvar.cloud2x - 1 > 0 and Globalvar.cloud2x - 1 < 90:
                self.layout[7][Globalvar.cloud2x - 1] = '('
            if Globalvar.cloud2x > 0 and Globalvar.cloud2x < 90:
                self.layout[7][Globalvar.cloud2x] = '_'
            if Globalvar.cloud2x + 5 > 0 and Globalvar.cloud2x + 5 < 90:
                self.layout[7][Globalvar.cloud2x + 5] = '_'
            if Globalvar.cloud2x + 6 > 0 and Globalvar.cloud2x + 6 < 90:
                self.layout[7][Globalvar.cloud2x + 6] = ')'

            '''Cloud3'''
            if Globalvar.cloud3x + 1 > 0 and Globalvar.cloud3x + 1 < 90:
                self.layout[5][Globalvar.cloud3x + 1] = '('
                self.layout[6][Globalvar.cloud3x + 1] = '_'
            if Globalvar.cloud3x + 2 > 0 and Globalvar.cloud3x + 2 < 90:
                self.layout[5][Globalvar.cloud3x + 2] = '_'
                self.layout[6][Globalvar.cloud3x + 2] = '_'
            if Globalvar.cloud3x + 3 > 0 and Globalvar.cloud3x + 3 < 90:
                self.layout[5][Globalvar.cloud3x + 3] = '_'
                self.layout[6][Globalvar.cloud3x + 3] = ')'
            if Globalvar.cloud3x + 4 > 0 and Globalvar.cloud3x + 4 < 90:
                self.layout[5][Globalvar.cloud3x + 4] = ')'
                self.layout[6][Globalvar.cloud3x + 4] = '_'
            if Globalvar.cloud3x - 1 > 0 and Globalvar.cloud3x - 1 < 90:
                self.layout[6][Globalvar.cloud3x - 1] = '('
            if Globalvar.cloud3x > 0 and Globalvar.cloud3x < 90:
                self.layout[6][Globalvar.cloud3x] = '_'
            if Globalvar.cloud3x + 5 > 0 and Globalvar.cloud3x + 5 < 90:
                self.layout[6][Globalvar.cloud3x + 5] = '_'
            if Globalvar.cloud3x + 6 > 0 and Globalvar.cloud3x + 6 < 90:
                self.layout[6][Globalvar.cloud3x + 6] = ')'

        '''Generating Enemies based on the checkpoints provided'''
        if Globalvar.GlobalX in EnemyCheckpoints:
            EnemyCheckpoints.remove(Globalvar.GlobalX)
            self.Enemyarr.append(enemy())

    def Bossfight(self, Mario, character, Globalvar):
        '''Updating Score'''
        self.layout[0][6] = str(self.score)[0]
        if self.score >= 10:
            self.layout[0][7] = str(self.score)[1]
        if self.score >= 100:
            self.layout[0][8] = str(self.score)[2]

        '''Coins'''
        self.layout[0][66] = str(self.coins)[0]
        if self.coins >= 10:
            self.layout[0][67] = str(self.coins)[1]

        '''Boss health'''
        self.layout[1][0:12] = 'Boss Health:'
        self.layout[1][12] = Boss.health

        '''Adding Ground'''
        for i in range(22, self.height):
            for j in range(self.width):
                self.layout[i][j] = 'X'

        '''Mario hurt'''
        if self.layout[Mario.posX][Mario.posY + 3] == '#' or self.layout[Mario.posX + 1][Mario.posY + 2] == '#':
            Boss.bulletarr.clear()
            Mario.lose(Globalvar, self.Enemyarr, self.Brickarr,
                       self.Coinarr, self.springarr, self.Pipearr)

        '''Actually moving mario'''

        '''Cheat'''
        if character == '9':
            Mario.lives += 1

        '''Shoot'''
        if character == ' ':
            if Mario.superpower:
                Mario.supershoot()
            else:
                Mario.supershoot()

        Mario.bossmove(character, Boss)

        '''Superjump'''
        if self.layout[Mario.posX + 2][Mario.posY] == '-':
            Mario.Superjump()

        if self.layout[Mario.posX + 2][Mario.posY] == 'X':
            Mario.inair = False

        if self.layout[Boss.posX + 3][Mario.posY] == 'X':
            Boss.inair = False

        '''Mario dead'''
        if Mario.lives == 0:
            self.gameover()

        '''Number of lives'''
        self.layout[0][46] = str(Mario.lives)

        '''Drawing Mario'''
        self.layout[Mario.posX][Mario.posY - 1] = '['
        self.layout[Mario.posX][Mario.posY] = 'M'
        self.layout[Mario.posX][Mario.posY + 1] = 'M'
        self.layout[Mario.posX][Mario.posY + 2] = ']'
        self.layout[Mario.posX + 1][Mario.posY] = '['
        self.layout[Mario.posX + 1][Mario.posY + 1] = ']'

        '''Boss hurt?'''
        try:
            if self.layout[Boss.posX][Boss.posY - 1] == '*' or self.layout[Boss.posX + 1][Boss.posY - 1] == '*' or \
                    [Boss.posX + 2][Boss.posY - 1] == '*':

                Boss.hurt += 1
                Boss.health -= 1
                for bulletx in Mario.bulletarr:
                    if bulletx[1] == Boss.posY - 1 and \
                            (bulletx[0] == Boss.posX or bulletx[0] == Boss.posX + 1 or bulletx[0] == Boss.posX + 2):

                        Mario.bulletarr.remove(bulletx)
                        break
                if Boss.hurt == 6:
                    self.won()
        except:
            pass

        '''Move boss'''
        choice = randint(1, 5)
        Boss.always()
        if choice == 1:
            Boss.moveright()
        elif choice == 2:
            Boss.moveleft()
        elif choice == 3:
            if Boss.inair == False:
                Boss.movejump()
        else:
            if randint(1, 6) == 4:
                Boss.shoot()

        '''Draw boss'''
        try:
            self.layout[Boss.posX][Boss.posY] = '('
        except:
            pass
        try:
            self.layout[Boss.posX][Boss.posY + 1] = ')'
        except:
            pass
        try:
            self.layout[Boss.posX + 1][Boss.posY] = '|'
        except:
            pass
        try:
            self.layout[Boss.posX + 1][Boss.posY + 1] = '|'
        except:
            pass
        try:
            self.layout[Boss.posX + 2][Boss.posY] = '/'
        except:
            pass
        try:
            self.layout[Boss.posX + 2][Boss.posY + 1] = '\\'
        except:
            pass

    def updatebricks(self, Globalvar):
        '''Drawing bricks'''
        for brickx in self.Brickarr:
            if brickx.posY > 0 and brickx.posY < 89:
                self.layout[brickx.posX][brickx.posY] = 'X'
            if brickx.posY + 1 > 0 and brickx.posY + 1 < 89:
                self.layout[brickx.posX][brickx.posY + 1] = 'X'
            if brickx.posY + 2 > 0 and brickx.posY + 2 < 89:
                self.layout[brickx.posX][brickx.posY + 2] = 'X'

    def updatecoins(self, Globalvar):
        '''Drawing Coins'''
        for coinx in self.Coinarr:
            if coinx.posY > 0 and coinx.posY < 89:
                self.layout[coinx.posX][coinx.posY] = '('
            if coinx.posY > 0 and coinx.posY < 89:
                self.layout[coinx.posX][coinx.posY + 1] = ')'

    def updateenemy(self, Mario, Globalvar):
        '''Moving the enemies'''
        for enemyx in self.Enemyarr:

            if enemyx.posY + 2 < 89 and enemyx.posY > 0:
                if self.layout[enemyx.posX][enemyx.posY + 2] == '|' and enemyx.dir == -1:
                    enemyx.dir = 1

            if enemyx.posY - 1 < 89 and enemyx.posY > 0:
                if self.layout[enemyx.posX][enemyx.posY - 1] == '|' and enemyx.dir == 1:
                    enemyx.dir = -1

            enemyx.move()

            '''Out of board'''
            if enemyx.posY < 0:
                self.Enemyarr.remove(enemyx)
                continue
            elif enemyx.posY > 88:
                continue

            '''Free fall'''
            if enemyx.inair == False:
                if self.layout[enemyx.posX + 1][enemyx.posY] == ' ':
                    enemyx.inair = True
                    enemyx.inairtime = 16

            '''Ground check'''
            if self.layout[enemyx.posX + 1][enemyx.posY] == 'X':
                enemyx.inair = False

            '''Drowning'''
            if self.layout[enemyx.posX + 1][enemyx.posY] == '~':
                self.Enemyarr.remove(enemyx)
                continue

            '''Shot dead'''
            if self.layout[enemyx.posX - 1][enemyx.posY - 1] == '*':
                self.Enemyarr.remove(enemyx)
                for bulletx in Mario.bulletarr:
                    if bulletx[1] == enemyx.posY - 1 and bulletx[0] == enemyx.posX - 1:
                        Mario.bulletarr.remove(bulletx)
                        break

                continue

            '''Stuck in ground'''
            try:
                if self.layout[enemyx.posX][enemyx.posY + 2] == 'X' and self.layout[enemyx.posX][enemyx.posY - 1] == 'X':
                    self.Enemyarr.remove(enemyx)
            except:
                pass

            '''Mario Jumping on enemy'''
            if self.layout[enemyx.posX - 3][enemyx.posY] == 'M' or self.layout[enemyx.posX - 3][enemyx.posY] == '[' and \
                    Mario.inairtime >= 16:

                self.Enemyarr.remove(enemyx)
                continue

            '''Mario collides with enemy'''
            if self.layout[enemyx.posX - 1][enemyx.posY - 1] == ']' and enemyx.dir == 1:
                Mario.lose(Globalvar, self.Enemyarr, self.Brickarr,
                           self.Coinarr, self.springarr, self.Pipearr)
            if enemyx.posY + 2 >= 0 and enemyx.posY + 2 < 89 and enemyx.dir == -1 and self.layout[enemyx.posX - 1][enemyx.posY + 2] == '[':
                Mario.lose(Globalvar, self.Enemyarr, self.Brickarr,
                           self.Coinarr, self.springarr, self.Pipearr)

            '''Drawing enemies'''
            if enemyx.posY >= 0 and enemyx.posY < 89:
                self.layout[enemyx.posX - 1][enemyx.posY] = '/'
                self.layout[enemyx.posX - 1][enemyx.posY + 1] = '\\'
                self.layout[enemyx.posX][enemyx.posY] = 'o'
                self.layout[enemyx.posX][enemyx.posY + 1] = 'o'

    def updatebullets(self, Mario):
        '''Mario bullets'''
        for bulletx in Mario.bulletarr:
            try:
                '''Enemy ahead'''
                if self.layout[bulletx[0]][bulletx[1] + 1] == '/' or self.layout[bulletx[0]][bulletx[1] + 1] == '\\':
                    for enemyx in self.Enemyarr:
                        if enemyx.posY == bulletx[1] + 1 or enemyx.posY + 1 == bulletx[1] + 1:
                            self.Enemyarr.remove(enemyx)
                            break
            except:
                pass
            try:
                '''Wall ahead'''
                if self.layout[bulletx[0]][bulletx[1] + 1] == 'X' or self.layout[bulletx[0]][bulletx[1] + 1] == '|':
                    Mario.bulletarr.remove(bulletx)
                    continue
            except:
                pass

            bulletx[1] += 1
            if bulletx[1] > 89:
                Mario.bulletarr.remove(bulletx)
                continue
            self.layout[bulletx[0]][bulletx[1]] = '*'

        '''Boss bullets'''
        for bulletx in Boss.bulletarr:
            bulletx[1] -= 1
            if bulletx[1] <= 0:
                Boss.bulletarr.remove(bulletx)
                continue
            self.layout[bulletx[0]][bulletx[1]] = '#'

    def updatepipes(self):

        for pipe in self.Pipearr:
            if pipe.posY > 0 and pipe.posY < 89:
                self.layout[pipe.posX + 1][pipe.posY] = '|'
                self.layout[pipe.posX + 2][pipe.posY] = '|'
                self.layout[pipe.posX + 3][pipe.posY] = '|'

            if pipe.posY + 4 > 0 and pipe.posY + 3 < 87:
                self.layout[pipe.posX][pipe.posY - 1:pipe.posY + 5] = '......'
                self.layout[pipe.posX + 1][pipe.posY + 3] = '|'
                self.layout[pipe.posX + 2][pipe.posY + 3] = '|'
                self.layout[pipe.posX + 3][pipe.posY + 3] = '|'

    def updatesprings(self):

        for springs in self.springarr:
            if springs.posY > 0 and springs.posY < 89:
                self.layout[springs.posX][springs.posY] = '-'
                self.layout[springs.posX + 2][springs.posY] = '/'
                self.layout[springs.posX + 1][springs.posY] = '\\'

            if springs.posY + 1 > 0 and springs.posY + 1 < 89:
                self.layout[springs.posX][springs.posY + 1] = '-'
                self.layout[springs.posX + 1][springs.posY + 1] = '/'
                self.layout[springs.posX + 2][springs.posY + 1] = '\\'

    def updatemario(self, Mario, Globalvar, character='l'):
        '''Putting Mario on the board and other things'''

        '''Cheat'''
        if character == '9':
            Mario.lives += 1

        '''Shoot'''
        if character == ' ':
            if Mario.superpower:
                Mario.supershoot()
            else:
                Mario.shoot()

        '''Wall ahead'''
        if self.layout[Mario.posX][Mario.posY + 3] == 'X' or self.layout[Mario.posX][Mario.posY + 3] == '|' or \
        	self.layout[Mario.posX + 1][Mario.posY + 3] == 'X' or self.layout[Mario.posX + 1][Mario.posY + 3] == '|':
            '''No forward movement'''
            if character == 'd':
                character = 'l'

        '''Wall behind'''
        if self.layout[Mario.posX][Mario.posY - 2] == 'X' or self.layout[Mario.posX][Mario.posY - 2] == '|':
            '''No backward movement'''
            if character == 'a':
                character = 'l'

        Mario.move(character, Globalvar, self.Enemyarr, self.Brickarr,
                   self.Coinarr, self.springarr, self.Pipearr)

        '''Superjump'''
        if self.layout[Mario.posX + 2][Mario.posY] == '-':
            Mario.Superjump()

        '''Free fall'''
        if Mario.inair == False:
            if self.layout[Mario.posX + 2][Mario.posY] == ' ':
                Mario.inair = True
                Mario.inairtime = 16

        '''Check for collisions'''
        if self.layout[Mario.posX + 2][Mario.posY] == 'X' or self.layout[Mario.posX + 2][Mario.posY + 1] == 'X' or \
                self.layout[Mario.posX + 2][Mario.posY - 1] == 'X' or self.layout[Mario.posX + 2][Mario.posY] == '.' or\
                self.layout[Mario.posX + 2][Mario.posY + 1] == '.':

            Mario.inair = False

        '''Drowning'''
        if self.layout[Mario.posX + 2][Mario.posY] == '~':
            Mario.lose(Globalvar, self.Enemyarr, self.Brickarr,
                       self.Coinarr, self.springarr, self.Pipearr)

        '''Stuck in ground'''
        if self.layout[Mario.posX + 1][Mario.posY + 2] == 'X' and self.layout[Mario.posX + 1][Mario.posY - 1] == 'X':
            Mario.lose(Globalvar, self.Enemyarr, self.Brickarr,
                       self.Coinarr, self.springarr, self.Pipearr)

        '''Head collision with brick'''
        if self.layout[Mario.posX - 1][Mario.posY] == 'X' or self.layout[Mario.posX - 1][Mario.posY + 1] == 'X' or \
                self.layout[Mario.posX - 1][Mario.posY - 1] == 'X':

            for brickx in self.Brickarr:
                if (brickx.posY == Mario.posY or brickx.posY == Mario.posY + 1) and brickx.posX + 1 == Mario.posX:
                    if brickx.breakable == True:
                        self.Brickarr.remove(brickx)
                        break
            Mario.inairtime = 16

        '''Collecting Coins'''
        if self.layout[Mario.posX + 1][Mario.posY - 1] == '(' or self.layout[Mario.posX + 1][Mario.posY + 2] == ')':
            for coinx in self.Coinarr:
                if (coinx.posY == Mario.posY + 1 or coinx.posY + 1 == Mario.posY - 1) and coinx.posX == Mario.posX + 1:
                    self.Coinarr.remove(coinx)
                    self.score += 10
                    self.coins += 1
                    break

        '''Mario dead'''
        if Mario.lives == 0:
            self.gameover()

        '''Number of lives'''
        self.layout[0][46] = str(Mario.lives)

        '''Checking for superpower'''
        if Mario.posX == 7 and Globalvar.GlobalX >= 213 and Globalvar.GlobalX <= 218:
            Mario.superpower = True
            self.Brickarr.append(brick("unbreakable", 6, 20))
            Mario.inairtime = 16

        '''Drawing Mario'''
        self.layout[Mario.posX][Mario.posY - 1] = '['
        self.layout[Mario.posX][Mario.posY] = 'M'
        self.layout[Mario.posX][Mario.posY + 1] = 'M'
        self.layout[Mario.posX][Mario.posY + 2] = ']'
        self.layout[Mario.posX + 1][Mario.posY] = '['
        self.layout[Mario.posX + 1][Mario.posY + 1] = ']'

    def gameover(self):
        '''End Game'''

        self.over = True
        print('Your final score is ' + str(self.score))
        print("Game Over")

    def won(self):
        '''Woohoo'''

        self.over = True
        print('You won')
