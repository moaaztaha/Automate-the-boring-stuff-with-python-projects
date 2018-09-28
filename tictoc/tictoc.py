#theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
# 1|2|3
# 4|5|6
# 7|8|9

#Comunicating with the system
import sys

#Main Board
backup = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

#Main Menu
def menu():
	print('1-Play')
	print('2-Exit')
	
	n = input()

	if n == '1':
		board = backup.copy()
		game(board)
	elif n == '2':
		sys.exit('GoodBye')
	else:
		print("Please choose a valid number")



#Printtting the board with the new changes (newBoard)
def printBoard(newBoard):
	print(newBoard['1'] + '|' + newBoard['2'] + '|' + newBoard['3'])
	print('--+--')
	print(newBoard['4'] + '|' + newBoard['5'] + '|' + newBoard['6'])
	print('--+--')
	print(newBoard['7'] + '|' + newBoard['8'] + '|' + newBoard['9'])

#The Game main function
def game(theBoard):
	Range  = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	#Player Character
	char = 'X'
	while True:
		print('+++++++++++++++++++++++++++++++++++++')
		print('Type 0 to Exit\n')
		printBoard(theBoard)
		print('\n' + char + ' Turn.')
		print("Where next?")
		move = input() 
		if move == '0':
			menu()
		else:	
			if move in Range:
				Range.remove(move)		
				theBoard[move] = char
				#Check if there is any winner
				if (theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ') or (theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ') or (theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ') or (theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ') or (theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ') or (theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ') or (theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ') or (theBoard['3'] == theBoard['5'] == theBoard['7'] != ' '):
					print(char + ' Won!!')
					print('+++++++++++++++++++++++++++++++++++++')
					#Back to the menu
					menu()
				#Switching Players
				if char == 'X':
					char = 'O'
				else:
					char = 'X'
			else:
				print('Please choose from:')
				#Print the rest of availabe choices
				print(*Range)
	printBoard(theBoard)


#Showing the main menu
menu()