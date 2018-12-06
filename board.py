'''

   |
   |
   |
30 |               Board      /\
   |                         /  \
   |XXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   |XXXXXXXXXXXX~~~XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   					90

This file contains the class
Board which contains and manages
the background board scenery '''

from random import randint
from enemy import Enemy
from brick import Brick
from coin import Coin
from boss import Boss
from spring import Spring
from pipe import Pipe

# Locations to spawn enemies
# If mario keeps standing in these positions infinitely many enemies will be spawned
ENEMYCHECKPOINTS = [
    60, 82, 87,
    170, 173, 175
]

BOSS = Boss()


class Board():
    '''Board class'''
    def __init__(self):
        '''Initialization'''
        self.over = False
        self.height = 30
        self.width = 90
        self.score = 0
        self.coins = 0
        self.layout = []
        self.enemyarr = []

        self.pipearr = [
            Pipe(18, 315), Pipe(18, 60),
            Pipe(18, 120), Pipe(18, 165)
        ]

        self.springarr = [
            Spring(19, 337), Spring(19, 390)
        ]

        self.brickarr = [
            Brick("unbreakable", 18, 37), Brick(
                "breakable", 18, 40),
            Brick("unbreakable", 18, 43), Brick(
                "breakable", 14, 40),
            Brick("breakable", 18, 113), Brick(
                "unbreakable", 14, 121),
            Brick("unbreakable", 10, 129), Brick(
                "unbreakable", 18, 235),
            Brick("unbreakable", 18, 225), Brick(
                "unbreakable", 18, 245),
            Brick("unbreakable", 14, 230), Brick(
                "unbreakable", 14, 240),
            Brick("breakable", 10, 235), Brick(
                "breakable", 10, 135),
            Brick("unbreakable", 14, 143), Brick(
                "unbreakable", 18, 151),
            Brick("unbreakable", 21, 340), Brick(
                "unbreakable", 13, 340),
            Brick("unbreakable", 20, 340), Brick(
                "unbreakable", 19, 340),
            Brick("unbreakable", 18, 340), Brick(
                "unbreakable", 17, 340),
            Brick("unbreakable", 16, 340), Brick(
                "unbreakable", 15, 340),
            Brick("unbreakable", 14, 340)
        ]

        self.coinarr = [
            Coin(21, 39), Coin(21, 41), Coin(21, 43), Coin(13, 40),
            Coin(9, 129), Coin(9, 235), Coin(13, 230), Coin(13, 240),
            Coin(17, 235)
        ]

        for _ in range(self.height):
            self.layout.append([])
        for i in range(self.height):
            for _ in range(self.width):
                self.layout[i].append(' ')

        # Fixed Score, lives and coins in the 1st row
        self.layout[0][0:6] = 'Score:'
        self.layout[0][40:46] = 'Lives:'
        self.layout[0][60:66] = 'Coins:'

    def updatebg(self, Globalvar):
        '''Score increment on forward movement'''
        self.score = max(self.score, Globalvar.globalx)

        # The base
        for i in range(1, self.height):
            for j in range(self.width):
                self.layout[i][j] = ' '

        # Updating The score
        self.layout[0][6] = str(self.score)[0]
        if self.score >= 10:
            self.layout[0][7] = str(self.score)[1]
        if self.score >= 100:
            self.layout[0][8] = str(self.score)[2]

        # Updating number of coins collected
        self.layout[0][66] = str(self.coins)[0]
        if self.coins >= 10:
            self.layout[0][67] = str(self.coins)[1]

        # Adding Ground
        for i in range(22, self.height):
            for j in range(self.width):
                self.layout[i][j] = 'X'

        # Adding Water
        if Globalvar.globalx < 300:
            for i in range(22, 25):
                for j in range(Globalvar.waterx, Globalvar.waterx + 10):
                    try:
                        self.layout[i][j] = ' '
                    except IndexError:
                        pass

            for i in range(25, self.height):
                for j in range(Globalvar.waterx, Globalvar.waterx + 10):
                    try:
                        self.layout[i][j] = '~'
                    except IndexError:
                        pass

        # Adding Mountains
        if Globalvar.globalx < 395:
            for i in range(5):
                if Globalvar.mountainx + i > 0 and Globalvar.mountainx + i < 90:
                    self.layout[21 - i][Globalvar.mountainx + i] = '/'
                if Globalvar.mountainx + 10 - i > 0 and Globalvar.mountainx + 10 - i < 90:
                    self.layout[21 - i][Globalvar.mountainx + 10 - i] = '\\'

        # Adding Clouds
        if Globalvar.globalx < 360:
            # Cloud1
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

            # Cloud2
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

            # Cloud3
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

        # Generating Enemies based on the checkpoints provided
        if Globalvar.globalx in ENEMYCHECKPOINTS:
            ENEMYCHECKPOINTS.remove(Globalvar.globalx)
            self.enemyarr.append(Enemy())

    def Bossfight(self, Mario, character, Globalvar):
        '''Updating Score'''
        self.layout[0][6] = str(self.score)[0]
        if self.score >= 10:
            self.layout[0][7] = str(self.score)[1]
        if self.score >= 100:
            self.layout[0][8] = str(self.score)[2]

        # coins
        self.layout[0][66] = str(self.coins)[0]
        if self.coins >= 10:
            self.layout[0][67] = str(self.coins)[1]

        # BOSS Health
        self.layout[1][0:12] = 'BOSS Health:'
        self.layout[1][12] = BOSS.health

        # Adding Ground
        for i in range(22, self.height):
            for j in range(self.width):
                self.layout[i][j] = 'X'

        # Mario hurt
        if self.layout[Mario.posx][Mario.posy + 3] == '#' \
        or self.layout[Mario.posx + 1][Mario.posy + 2] == '#':
            BOSS.bulletarr.clear()
            Mario.lose(Globalvar, self.enemyarr, self.brickarr,
                       self.coinarr, self.springarr, self.pipearr)

        # Actually moving mario

        # Cheat
        if character == '9':
            Mario.lives += 1

        # Shoot
        if character == ' ':
            if Mario.superpower:
                Mario.supershoot()
            else:
                Mario.supershoot()

        Mario.bossmove(character, BOSS)

        # Superjump
        if self.layout[Mario.posx + 2][Mario.posy] == '-':
            Mario.Superjump()

        if self.layout[Mario.posx + 2][Mario.posy] == 'X':
            Mario.inair = False

        if self.layout[BOSS.posX + 3][Mario.posy] == 'X':
            BOSS.inair = False

        # Mario dead
        if Mario.lives == 0:
            self.gameover()

        # Number of lives
        self.layout[0][46] = str(Mario.lives)

        # Drawing Mario
        self.layout[Mario.posx][Mario.posy - 1] = '['
        self.layout[Mario.posx][Mario.posy] = 'M'
        self.layout[Mario.posx][Mario.posy + 1] = 'M'
        self.layout[Mario.posx][Mario.posy + 2] = ']'
        self.layout[Mario.posx + 1][Mario.posy] = '['
        self.layout[Mario.posx + 1][Mario.posy + 1] = ']'

        # BOSS hurt?
        try:
            if self.layout[BOSS.posX][BOSS.posY - 1] == '*' \
            or self.layout[BOSS.posX + 1][BOSS.posY - 1] == '*' \
            or [BOSS.posX + 2][BOSS.posY - 1] == '*':

                BOSS.hurt += 1
                BOSS.health -= 1
                for bulletx in Mario.bulletarr:
                    if bulletx[1] == BOSS.posY - 1 and \
                            (bulletx[0] == BOSS.posX or bulletx[0] == BOSS.posX + 1 \
                                or bulletx[0] == BOSS.posX + 2):

                        Mario.bulletarr.remove(bulletx)
                        break
                if BOSS.hurt == 6:
                    self.won()
        except IndexError:
            pass

        # Move BOSS
        choice = randint(1, 5)
        BOSS.always()
        if choice == 1:
            BOSS.moveright()
        elif choice == 2:
            BOSS.moveleft()
        elif choice == 3:
            if not BOSS.inair:
                BOSS.movejump()
        else:
            if randint(1, 6) == 4:
                BOSS.shoot()

        # Draw BOSS
        try:
            self.layout[BOSS.posX][BOSS.posY] = '('
        except IndexError:
            pass
        try:
            self.layout[BOSS.posX][BOSS.posY + 1] = ')'
        except IndexError:
            pass
        try:
            self.layout[BOSS.posX + 1][BOSS.posY] = '|'
        except IndexError:
            pass
        try:
            self.layout[BOSS.posX + 1][BOSS.posY + 1] = '|'
        except IndexError:
            pass
        try:
            self.layout[BOSS.posX + 2][BOSS.posY] = '/'
        except IndexError:
            pass
        try:
            self.layout[BOSS.posX + 2][BOSS.posY + 1] = '\\'
        except IndexError:
            pass

    def updatebricks(self, Globalvar):
        '''Drawing Bricks'''
        for Brickx in self.brickarr:
            if Brickx.posy > 0 and Brickx.posy < 89:
                self.layout[Brickx.posx][Brickx.posy] = 'X'
            if Brickx.posy + 1 > 0 and Brickx.posy + 1 < 89:
                self.layout[Brickx.posx][Brickx.posy + 1] = 'X'
            if Brickx.posy + 2 > 0 and Brickx.posy + 2 < 89:
                self.layout[Brickx.posx][Brickx.posy + 2] = 'X'

    def updatecoins(self, Globalvar):
        '''Drawing coins'''
        for Coinx in self.coinarr:
            if Coinx.posy > 0 and Coinx.posy < 89:
                self.layout[Coinx.posx][Coinx.posy] = '('
            if Coinx.posy > 0 and Coinx.posy < 89:
                self.layout[Coinx.posx][Coinx.posy + 1] = ')'

    def updateenemy(self, Mario, Globalvar):
        '''Moving the enemies'''
        for Enemyx in self.enemyarr:

            if Enemyx.posy + 2 < 89 and Enemyx.posy > 0:
                if self.layout[Enemyx.posx][Enemyx.posy + 2] == '|' and Enemyx.dir == -1:
                    Enemyx.dir = 1

            if Enemyx.posy - 1 < 89 and Enemyx.posy > 0:
                if self.layout[Enemyx.posx][Enemyx.posy - 1] == '|' and Enemyx.dir == 1:
                    Enemyx.dir = -1

            Enemyx.move()

            # Out of board
            if Enemyx.posy < 0:
                self.enemyarr.remove(Enemyx)
                continue
            elif Enemyx.posy > 88:
                continue

            # Free fall
            if not Enemyx.inair:
                if self.layout[Enemyx.posx + 1][Enemyx.posy] == ' ':
                    Enemyx.inair = True
                    Enemyx.inairtime = 16

            # Ground check
            if self.layout[Enemyx.posx + 1][Enemyx.posy] == 'X':
                Enemyx.inair = False

            # Drowning
            if self.layout[Enemyx.posx + 1][Enemyx.posy] == '~':
                self.enemyarr.remove(Enemyx)
                continue

            # Shot dead
            if self.layout[Enemyx.posx - 1][Enemyx.posy - 1] == '*' \
            or self.layout[Enemyx.posx - 1][Enemyx.posy] == '*':
                self.enemyarr.remove(Enemyx)
                for bulletx in Mario.bulletarr:
                    if bulletx[1] == Enemyx.posy - 1 and bulletx[0] == Enemyx.posx - 1:
                        Mario.bulletarr.remove(bulletx)
                        break

                continue

            # Stuck in ground
            try:
                if self.layout[Enemyx.posx][Enemyx.posy + 2] == 'X' \
                and self.layout[Enemyx.posx][Enemyx.posy - 1] == 'X':
                    self.enemyarr.remove(Enemyx)
            except:
                pass

            # Mario Jumping on Enemy
            if self.layout[Enemyx.posx - 3][Enemyx.posy] == 'M' \
            or self.layout[Enemyx.posx - 3][Enemyx.posy] == '[' and     Mario.inairtime >= 16:

                self.enemyarr.remove(Enemyx)
                continue

            # Mario collides with Enemy
            if self.layout[Enemyx.posx - 1][Enemyx.posy - 1] == ']' and Enemyx.dir == 1:
                Mario.lose(Globalvar, self.enemyarr, self.brickarr,
                           self.coinarr, self.springarr, self.pipearr)
            if Enemyx.posy + 2 >= 0 and Enemyx.posy + 2 < 89 and Enemyx.dir == -1 \
            and self.layout[Enemyx.posx - 1][Enemyx.posy + 2] == '[':
                Mario.lose(Globalvar, self.enemyarr, self.brickarr,
                           self.coinarr, self.springarr, self.pipearr)

            # Drawing enemies
            if Enemyx.posy >= 0 and Enemyx.posy < 89:
                self.layout[Enemyx.posx - 1][Enemyx.posy] = '/'
                self.layout[Enemyx.posx - 1][Enemyx.posy + 1] = '\\'
                self.layout[Enemyx.posx][Enemyx.posy] = 'o'
                self.layout[Enemyx.posx][Enemyx.posy + 1] = 'o'

    def updatebullets(self, Mario):
        '''Mario bullets'''
        for bulletx in Mario.bulletarr:
            try:
                # Enemy ahead
                if self.layout[bulletx[0]][bulletx[1] + 1] == '/' \
                or self.layout[bulletx[0]][bulletx[1] + 1] == '\\':
                    for Enemyx in self.enemyarr:
                        if Enemyx.posy == bulletx[1] + 1 or Enemyx.posy == bulletx[1]:
                            self.enemyarr.remove(Enemyx)
                            break
            except:
                pass
            try:
                # Wall ahead
                if self.layout[bulletx[0]][bulletx[1] + 1] == 'X' \
                or self.layout[bulletx[0]][bulletx[1] + 1] == '|':
                    Mario.bulletarr.remove(bulletx)
                    continue
            except IndexError:
                pass

            bulletx[1] += 1
            if bulletx[1] > 89:
                Mario.bulletarr.remove(bulletx)
                continue
            self.layout[bulletx[0]][bulletx[1]] = '*'

        # BOSS bullets
        for bulletx in BOSS.bulletarr:
            bulletx[1] -= 1
            if bulletx[1] <= 0:
                BOSS.bulletarr.remove(bulletx)
                continue
            self.layout[bulletx[0]][bulletx[1]] = '#'

    def updatepipes(self):
        '''Update the pipes'''
        for Pipe in self.pipearr:
            if Pipe.posy > 0 and Pipe.posy < 89:
                self.layout[Pipe.posx + 1][Pipe.posy] = '|'
                self.layout[Pipe.posx + 2][Pipe.posy] = '|'
                self.layout[Pipe.posx + 3][Pipe.posy] = '|'

            if Pipe.posy + 4 > 0 and Pipe.posy + 3 < 87:
                self.layout[Pipe.posx][Pipe.posy - 1:Pipe.posy + 5] = '......'
                self.layout[Pipe.posx + 1][Pipe.posy + 3] = '|'
                self.layout[Pipe.posx + 2][Pipe.posy + 3] = '|'
                self.layout[Pipe.posx + 3][Pipe.posy + 3] = '|'

    def updatesprings(self):
        '''Update the springs'''
        for springs in self.springarr:
            if springs.posy > 0 and springs.posy < 89:
                self.layout[springs.posx][springs.posy] = '-'
                self.layout[springs.posx + 2][springs.posy] = '/'
                self.layout[springs.posx + 1][springs.posy] = '\\'

            if springs.posy + 1 > 0 and springs.posy + 1 < 89:
                self.layout[springs.posx][springs.posy + 1] = '-'
                self.layout[springs.posx + 1][springs.posy + 1] = '/'
                self.layout[springs.posx + 2][springs.posy + 1] = '\\'

    def updatemario(self, Mario, Globalvar, character='l'):
        '''Putting Mario on the board and other things'''

        # Cheat
        if character == '9':
            Mario.lives += 1

        # Shoot
        if character == ' ':
            if Mario.superpower:
                Mario.supershoot()
            else:
                Mario.shoot()

        # Wall ahead
        if self.layout[Mario.posx][Mario.posy + 3] == 'X' \
        or self.layout[Mario.posx][Mario.posy + 3] == '|' \
        or self.layout[Mario.posx + 1][Mario.posy + 3] == 'X' \
            or self.layout[Mario.posx + 1][Mario.posy + 3] == '|':
            # No forward movement
            if character == 'd':
                character = 'l'

        # Wall behind
        if self.layout[Mario.posx][Mario.posy - 2] == 'X' \
        or self.layout[Mario.posx][Mario.posy - 2] == '|':
            # No backward movement
            if character == 'a':
                character = 'l'

        # Collecting coins
        if self.layout[Mario.posx + 1][Mario.posy - 1] == '(' \
        or self.layout[Mario.posx + 1][Mario.posy + 2] == ')':
            for Coinx in self.coinarr:
                if (Coinx.posy == Mario.posy + 1 or Coinx.posy + 1 == Mario.posy - 1) \
                and Coinx.posx == Mario.posx + 1:
                    self.coinarr.remove(Coinx)
                    self.score += 10
                    self.coins += 1
                    break

        # Added code
        if self.layout[Mario.posx + 2][Mario.posy] == '(' \
	    or self.layout[Mario.posx + 2][Mario.posy + 1] == '(':
            for Coinx in self.coinarr:
                if (Coinx.posy == Mario.posy + 1 or Coinx.posy == Mario.posy ) \
                and Coinx.posx == Mario.posx + 2:
                    self.coinarr.remove(Coinx)
                    self.score += 10
                    self.coins += 1
                    break        

        Mario.move(character, Globalvar, self.enemyarr, self.brickarr,
                   self.coinarr, self.springarr, self.pipearr)

        # Superjump
        if self.layout[Mario.posx + 2][Mario.posy] == '-':
            Mario.Superjump()

        # Free fall
        if not Mario.inair:
            if self.layout[Mario.posx + 2][Mario.posy] == ' ':
                Mario.inair = True
                Mario.inairtime = 16

        # Check for collisions
        if self.layout[Mario.posx + 2][Mario.posy] == 'X' \
        or self.layout[Mario.posx + 2][Mario.posy + 1] == 'X' or \
        self.layout[Mario.posx + 2][Mario.posy - 1] == 'X' \
        or self.layout[Mario.posx + 2][Mario.posy] == '.' or\
        self.layout[Mario.posx + 2][Mario.posy + 1] == '.':

            Mario.inair = False

        # Drowning
        if self.layout[Mario.posx + 2][Mario.posy] == '~':
            Mario.lose(Globalvar, self.enemyarr, self.brickarr,
                       self.coinarr, self.springarr, self.pipearr)

        # Stuck in ground
        if self.layout[Mario.posx + 1][Mario.posy + 2] == 'X' \
        and self.layout[Mario.posx + 1][Mario.posy - 1] == 'X':
            Mario.lose(Globalvar, self.enemyarr, self.brickarr,
                       self.coinarr, self.springarr, self.pipearr)

        # Head collision with Brick
        if self.layout[Mario.posx - 1][Mario.posy] == 'X' \
        or self.layout[Mario.posx - 1][Mario.posy + 1] == 'X' or \
                self.layout[Mario.posx - 1][Mario.posy - 1] == 'X':

            for Brickx in self.brickarr:
                if (Brickx.posy == Mario.posy or Brickx.posy == Mario.posy + 1) \
                and Brickx.posx + 1 == Mario.posx:
                    if Brickx.breakable:
                        self.brickarr.remove(Brickx)
                        break
            Mario.inairtime = 16

        # Mario dead
        if Mario.lives == 0:
            self.gameover()

        # Number of lives
        self.layout[0][46] = str(Mario.lives)

        # Checking for superpower
        if Mario.posx == 7 and Globalvar.globalx >= 213 and Globalvar.globalx <= 218:
            Mario.superpower = True
            self.brickarr.append(Brick("unbreakable", 6, 20))
            Mario.inairtime = 16

        # Drawing Mario
        self.layout[Mario.posx][Mario.posy - 1] = '['
        self.layout[Mario.posx][Mario.posy] = 'M'
        self.layout[Mario.posx][Mario.posy + 1] = 'M'
        self.layout[Mario.posx][Mario.posy + 2] = ']'
        self.layout[Mario.posx + 1][Mario.posy] = '['
        self.layout[Mario.posx + 1][Mario.posy + 1] = ']'

    def gameover(self):
        '''End Game'''

        self.over = True
        print('Your final score is ' + str(self.score))
        print("Game Over")

    def won(self):
        '''Woohoo'''

        self.over = True
        print('You won')
