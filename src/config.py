'''Contains The globalvarl
   scenery position'''


class Globalvar():

    '''Global configuration'''

    def __init__(self):
        '''Initialization'''
        self.globalx = 0
        self.waterx = 89
        self.cloudx = 32
        self.cloud2x = 35
        self.cloud3x = 47
        self.mountainx = 28

    def update(self, character, Enemyarr, brickarr, coinarr, springarr, pipearr):

        '''Moving scene elements'''

        if character == 'a':
            # Handling scene elements
            if self.globalx > 0:
                self.globalx -= 1

                self.waterx += 1
                if self.waterx == 89:
                    self.waterx = -15

                self.mountainx += 1
                if self.mountainx == 89:
                    self.mountainx = -9

                self.cloudx += 1
                if self.cloudx == 89:
                    self.cloudx = -6

                self.cloud2x += 1
                if self.cloud2x == 89:
                    self.cloud2x = -6

                self.cloud3x += 1
                if self.cloud3x == 89:
                    self.cloud3x = -6

                for enemyx in Enemyarr:
                    enemyx.posy += 1

                for brickx in brickarr:
                    brickx.posy += 1

                for coinx in coinarr:
                    coinx.posy += 1

                for springs in springarr:
                    springs.posy += 1

                for pipe in pipearr:
                    pipe.posy += 1

        elif character == 'd':

            # Handling scene elements
            self.globalx += 1

            self.waterx -= 1
            if self.waterx == -15:
                self.waterx = 89

            self.mountainx -= 1
            if self.mountainx == -9:
                self.mountainx = 89

            self.cloudx -= 1
            if self.cloudx == -5:
                self.cloudx = 89

            self.cloud2x -= 1
            if self.cloud2x == -5:
                self.cloud2x = 89

            self.cloud3x -= 1
            if self.cloud3x == -5:
                self.cloud3x = 89

            for enemyx in Enemyarr:
                enemyx.posy -= 1

            for brickx in brickarr:
                brickx.posy -= 1

            for coinx in coinarr:
                coinx.posy -= 1

            for springs in springarr:
                springs.posy -= 1

            for pipe in pipearr:
                pipe.posy -= 1
