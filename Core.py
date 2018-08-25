''' This file contains the main game loop
	where the update functions are being called '''

import os
from Board import board
from Mario import mario
import signal
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from Config import globalvar
from colorama import *

'''Music'''
try:
	os.system("aplay music.wav &")
except:
	pass


'''Input functions'''

def alarmhandler(signum, frame):
    ''' input method '''
    raise AlarmException


def user_input(timeout=0.1):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


''' Clearing the screen for the game'''
os.system('clear')

print('Welcome to Mario')

'''Instance Of Board Class'''
Board = board()
'''Instance of Mario Class'''
Mario = mario()
'''Instance of globalvar Class'''
Globalvar = globalvar()

''' The main game loop'''
while True:

    char = user_input()

    if char == 'q':
        '''Quit Game'''
        try:
        	os.system("killall -9 aplay")
        except:
        	pass
        print('Thanks for Playing')
        break

    else:

        '''Boss fight'''
        if Globalvar.GlobalX == 370:

            '''The base board'''
            for i in range(1, Board.height):
                for j in range(Board.width):
                    Board.layout[i][j] = ' '

            Board.updatebullets(Mario)
            Board.updatesprings()
            Board.Bossfight(Mario, char, Globalvar)

        else:
            '''Normal fight'''
            Board.updatebg(Globalvar)
            Board.updatebricks(Globalvar)
            Board.updatecoins(Globalvar)
            Board.updatepipes()
            Board.updatebullets(Mario)
            Board.updatesprings()
            Board.updatemario(Mario, Globalvar, char)
            Board.updateenemy(Mario, Globalvar)

        if Board.over == True:
        	try:
        		os.system("killall -9 aplay")
        	except:
        		pass
        	break

        '''Drawing The board'''
        os.system('clear')

        for i in range(Board.height):
            for j in range(Board.width):
                '''Printing with colors'''
                if Board.layout[i][j] == 'M' or Board.layout[i][j] == '[' or Board.layout[i][j] == ']' or Board.layout[i][j] == 'o' or \
                	Board.layout[i][j] == 'S' or Board.layout[i][j] == 'c':
                    print(Fore.RED + Board.layout[i][j], end=''),
                elif Board.layout[i][j] == '*':
                    print(Fore.CYAN + Board.layout[i][j], end=''),
                elif Board.layout[i][j] == 'X' or Board.layout[i][j] == '.':
                    print(Fore.YELLOW + Board.layout[i][j], end=''),
                elif Board.layout[i][j] == '~':
                    print(Fore.BLUE + Board.layout[i][j], end=''),
                elif Board.layout[i][j] == '\\' or Board.layout[i][j] == '/' or Board.layout[i][j] == '|':
                    print(Fore.GREEN + Board.layout[i][j], end=''),
                elif Board.layout[i][j] == '_' or Board.layout[i][j] == '(' or Board.layout[i][j] == ')':
                    print(Fore.WHITE + Board.layout[i][j], end=''),
                else:
                    print(Board.layout[i][j], end=''),
            print()
