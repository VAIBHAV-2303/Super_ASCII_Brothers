''' This file contains the main game loop
	where the update functions are being called '''

import os
import signal
import colorama
from board import Board
from mario import Mario
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from config import Globalvar

# Music
os.system("aplay music.wav &")

# Input functions

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


# Clearing the screen for the game
os.system('clear')

print('Welcome to MARIO')

# Instance Of BOARD Class
BOARD = Board()
'''Instance of MARIO Class'''
MARIO = Mario()
'''Instance of GLOBALVAR Class'''
GLOBALVAR = Globalvar()

''' The main game loop'''
while True:

    CHAR = user_input()

    if CHAR == 'q':
        # Quit Game
        os.system("killall -9 aplay")
        print('Thanks for Playing')
        break

    else:

        # Boss fight
        if GLOBALVAR.globalx == 370:

            # The base BOARD
            for i in range(1, BOARD.height):
                for j in range(BOARD.width):
                    BOARD.layout[i][j] = ' '

            BOARD.updatebullets(MARIO)
            BOARD.updatesprings()
            BOARD.Bossfight(MARIO, CHAR, GLOBALVAR)

        else:
            # Normal fight
            BOARD.updatebg(GLOBALVAR)
            BOARD.updatebricks(GLOBALVAR)
            BOARD.updatecoins(GLOBALVAR)
            BOARD.updatepipes()
            BOARD.updatebullets(MARIO)
            BOARD.updatesprings()
            BOARD.updatemario(MARIO, GLOBALVAR, CHAR)
            BOARD.updateenemy(MARIO, GLOBALVAR)

        if BOARD.over:
            os.system("killall -9 aplay")
            break

        # Drawing The BOARD
        os.system('clear')

        for i in range(BOARD.height):
            for j in range(BOARD.width):
                # Printing with colors
                if BOARD.layout[i][j] == 'M' or BOARD.layout[i][j] == '[' \
                 or BOARD.layout[i][j] == ']' or BOARD.layout[i][j] == 'o' \
                 or BOARD.layout[i][j] == 'S' or BOARD.layout[i][j] == 'c':
                    print(colorama.Fore.RED + BOARD.layout[i][j], end='')
                elif BOARD.layout[i][j] == '*':
                    print(colorama.Fore.CYAN + BOARD.layout[i][j], end='')
                elif BOARD.layout[i][j] == 'X' or BOARD.layout[i][j] == '.':
                    print(colorama.Fore.YELLOW + BOARD.layout[i][j], end='')
                elif BOARD.layout[i][j] == '~':
                    print(colorama.Fore.BLUE + BOARD.layout[i][j], end='')
                elif BOARD.layout[i][j] == '\\' or BOARD.layout[i][j] == '/'\
                 or BOARD.layout[i][j] == '|':
                    print(colorama.Fore.GREEN + BOARD.layout[i][j], end='')
                elif BOARD.layout[i][j] == '_' or BOARD.layout[i][j] == '('\
                 or BOARD.layout[i][j] == ')':
                    print(colorama.Fore.WHITE + BOARD.layout[i][j], end='')
                else:
                    print(BOARD.layout[i][j], end='')
            print()
