'''Contains The globalvarl 
   scenery position'''


class globalvar():

    def __init__(self):
        '''Initialization'''
        self.GlobalX = 0
        self.waterx = 89
        self.cloudx = 32
        self.cloud2x = 35
        self.cloud3x = 47
        self.Mountainx = 28

    def update(self, character, Enemyarr, Brickarr, Coinarr, springarr, Pipearr):

        if character == 'a':
            ''' Handling scene elements'''
            if self.GlobalX > 0:
                self.GlobalX -= 1

                self.waterx += 1
                if self.waterx == 89:
                    self.waterx = -15

                self.Mountainx += 1
                if self.Mountainx == 89:
                    self.Mountainx = -9

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
                    enemyx.posY += 1

                for brickx in Brickarr:
                    brickx.posY += 1

                for coinx in Coinarr:
                    coinx.posY += 1

                for springs in springarr:
                    springs.posY += 1

                for pipe in Pipearr:
                    pipe.posY += 1

        elif character == 'd':

            ''' Handling scene elements'''
            self.GlobalX += 1

            self.waterx -= 1
            if self.waterx == -15:
                self.waterx = 89

            self.Mountainx -= 1
            if self.Mountainx == -9:
                self.Mountainx = 89

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
                enemyx.posY -= 1

            for brickx in Brickarr:
                brickx.posY -= 1

            for coinx in Coinarr:
                coinx.posY -= 1

            for springs in springarr:
                springs.posY -= 1

            for pipe in Pipearr:
                pipe.posY -= 1
