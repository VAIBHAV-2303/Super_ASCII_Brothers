'''
	.....
	|   |
	|   |
	|   |

Contains the pipe class'''


class Pipe():
    '''Pipe class'''

    def __init__(self, x, y):
        '''Initialization'''
        self.__posx = x
        self.__posy = y

    @property
    def posx(self):
        '''getter'''
        return self.__posx

    @posx.setter
    def posx(self, value):
        self.__posx = value

    @property
    def posy(self):
        '''getter'''
        return self.__posy

    @posy.setter
    def posy(self, value):
        self.__posy = value
