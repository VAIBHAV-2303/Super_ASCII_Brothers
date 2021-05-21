'''Board module testing'''

import pytest
import colorama
from board import Board
from mario import Mario
from config import Globalvar
from enemy import Enemy

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

def movefw(BOARD, GLOBALVAR, MARIO, steps):
	for _ in range(steps):
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'd')
		BOARD.updateenemy(MARIO, GLOBALVAR)

def jump(BOARD, GLOBALVAR, MARIO):
	BOARD.updatebg(GLOBALVAR)
	BOARD.updatebricks(GLOBALVAR)
	BOARD.updatecoins(GLOBALVAR)
	BOARD.updatepipes()
	BOARD.updatebullets(MARIO)
	BOARD.updatesprings()
	BOARD.updatemario(MARIO, GLOBALVAR, 'w')
	BOARD.updateenemy(MARIO, GLOBALVAR)

def test_score_update():
	BOARD = Board()
	MARIO = Mario()
	GLOBALVAR = Globalvar()

	movefw(BOARD, GLOBALVAR, MARIO, 38)

	assert BOARD.score >= 30

def test_coin_collection():
	BOARD = Board()
	MARIO = Mario()
	GLOBALVAR = Globalvar()
	initial_size = len(BOARD.coinarr)


	# Moving mario to the first coin
	for i in range(20):
		if i == 10:
			print_board(BOARD)
			print('===============================================')
			print('Initial stage')
			print('===============================================')
		movefw(BOARD, GLOBALVAR, MARIO, 1)	

	print_board(BOARD)
	print('===========================================')
	print('Coins collected still 0')
	print('===========================================')

	assert len(BOARD.coinarr) == initial_size - 1

def test_respawning():
	BOARD = Board()
	MARIO = Mario()
	GLOBALVAR = Globalvar()

	movefw(BOARD, GLOBALVAR, MARIO, 38)	
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 28)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 26)
	
	MARIO.lose(GLOBALVAR, BOARD.enemyarr, BOARD.brickarr, BOARD.coinarr, BOARD.springarr, BOARD.pipearr)
	print_board(BOARD)
	print('=============================================================')
	print('Forcefully killed!!')
	print('=============================================================')

	for i in range(10):
		if i == 2:
			print_board(BOARD)
			print('==============================================================')
			print('Drowning after respawning and hence another life lost!!')
			print('==============================================================')
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'l')
		BOARD.updateenemy(MARIO, GLOBALVAR)

	print_board(BOARD)
	print('================================================')
	print('Final stage')
	print('================================================')
	assert MARIO.lives == 2

def test_killing_enemy():
	BOARD = Board()
	MARIO = Mario()
	GLOBALVAR = Globalvar()

	movefw(BOARD, GLOBALVAR, MARIO, 38)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 28)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 39)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 51)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 30)
	jump(BOARD, GLOBALVAR, MARIO)
	movefw(BOARD, GLOBALVAR, MARIO, 22)

	print_board(BOARD)
	print('========================================')
	print('3 Enemies exist')
	print('========================================')

	for i in range(9):
		if i%3 == 0:
			MARIO.shoot()
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'l')
		BOARD.updateenemy(MARIO, GLOBALVAR)

	print_board(BOARD)
	print('========================================')
	print('3 Shots fired')
	print('========================================')

	for i in range(22):
		BOARD.updatebg(GLOBALVAR)
		BOARD.updatebricks(GLOBALVAR)
		BOARD.updatecoins(GLOBALVAR)
		BOARD.updatepipes()
		BOARD.updatebullets(MARIO)
		BOARD.updatesprings()
		BOARD.updatemario(MARIO, GLOBALVAR, 'l')
		BOARD.updateenemy(MARIO, GLOBALVAR)	

	print_board(BOARD)
	print('=====================================')
	print('One enemy still alive')
	print('=====================================')
	
	assert len(BOARD.enemyarr) == 0