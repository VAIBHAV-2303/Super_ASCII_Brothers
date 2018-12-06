'''Config module testing'''

import pytest
import colorama
from board import Board
from mario import Mario
from config import Globalvar

def print_board(BOARD):
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


def test_scene_movement():
	GLOBALVAR = Globalvar()
	BOARD = Board()
	MARIO = Mario()

	for i in range(5):
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'd')
		BOARD.updateenemy(MARIO, GLOBALVAR)		

	initial_board = [0 for _ in range(30)]

	for i in range(30):
		initial_board[i] = BOARD.layout[i][:]
	
	print_board(BOARD)
	print('======================================')
	print('Initial postion')
	print('======================================')

	# Forward movement
	for i in range(6):
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'd')
		BOARD.updateenemy(MARIO, GLOBALVAR)

	print_board(BOARD)
	print('========================================')
	print('Moving 6 steps forward')
	print('========================================')

	# Backward movement
	for i in range(6):
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'a')
		BOARD.updateenemy(MARIO, GLOBALVAR)

	print_board(BOARD)
	print('=========================================')
	print('Moving 6 steps backward')
	print('=========================================')

	for i in range(1, 30):
		for j in range(90):
			assert initial_board[i][j] == BOARD.layout[i][j]
