import random
import os


#assign variables(rows, columns, players, checkers)
num_rows = 6
num_columns = 7
board =[]
num_players = 2
checkers = ["\bX", "\bO", "\bV", "\bH", "\bM"]
valid_moves = num_rows * num_columns

#assign random player
turn = random.randint(0, num_players-1)


#create board
for row in range(num_rows):
	row_list = []
	for col in range(num_columns): 
		row_list.append("")
	board.append(row_list)	

#check from the checker placed


#function: print board
def print_board():
	for x in range (num_columns):
		print(" " + chr(x+65), end='  ')   #use ascii code 
	print()
	for r in range(num_rows):
		for c in range(num_columns):
			print("+---", end = "")
		print("+", end= "")
		print()	
		for c in range(num_columns):
			print("|  ", end = "")
			print(board[r][c], end= " ")	
		print("|", end = "")
		print()	
	for c in range(num_columns):
		print("+---", end = "")
	print("+")


#function: check if column is full 
def check_full_column(coordinate):
	flag = 0
	for row in range(num_rows):
		if(board[row][coordinate] == ""):
			flag = 1
	return flag


#function: check vertical win
def check_vertical_win(turn):
	for i in range(num_columns):
		count = 0
		for j in range(num_rows):
			if(board[j][i] == checkers[turn]):
				count +=1
			else:
				count = 0
			if(count == 4):
				return True
	return False

#function: check horizontal win
def check_horizontal_win(turn):
	for i in range (num_rows):
		count = 0
		for j in range(num_columns):
			if(board[i][j]== checkers[turn]):
				count += 1
			else:
				count = 0
			if(count ==4):
				return True
	return False


#function: check diagonal win (direction: top left to right bottom, area: left bottom side)
def check_diagonal_win1(turn):
	for i in range(num_rows-3):
		count = 0
		y = i
		x = 0
		while(y < num_rows):
			if(board[y][x] == checkers[turn]):
				count += 1
			else:
				count = 0
			if(count == 4):
				return True
			y+=1
			x+=1

	return False

#function: check diagonal win (direction: top left to right bottom, area: right upper side)
def check_diagonal_win2(turn):
	for i in range(1,num_columns-3):
		count = 0
		y = 0
		x = i
		while(x < num_columns):
			if(board[y][x] == checkers[turn]):
				count +=1
			else:
				count = 0
			if(count == 4):
				return True
			y +=1
			x +=1

	return False


#function: check diagonal win (direction: top right to left bottom, area: left upper side)
def check_diagonal_win3(turn):
	for i in range (3, num_columns-1):
		count = 0
		y = 0
		x = i
		while(x >= 0):
			if(board[y][x] == checkers[turn]):
				count += 1
			else:
				count = 0
			if(count ==4):
				return True
			y +=1
			x -=1

	return False


#function: check diagonal win (direction: top right to left bottom, area: right bottom side)
def check_diagonal_win4(turn):
	for i in range(num_rows-3):
		count = 0
		y = i
		x = 6
		while(y < num_rows):
			if(board[y][x] == checkers[turn]):
				count += 1
			else:
				count = 0
			if(count ==4):
				return True
			y +=1
			x -=1
	return False

#print board before game
print_board()

#set win condition variable
win = False

#set while loop end condition as valid_moves>0 in case of draw
while(valid_moves>0):
	#os.system("clear")
	while(True):   #repeat until valid coordinate is input
		choice = input(checkers[turn] + " enter column to insert : ")
		if(len(choice) != 1 or choice.isalpha() == False):   #check if input length is one and is an alphabet
			print("please reenter column")
			continue      #repeat loop
		alph = choice.upper()   #convert alphabet into uppercase
		coordinate= int(ord(alph)-65)    #convert alphabet into integers to use as coordinates
		if(coordinate >= num_columns):   #check if coordinate is within the given columns
			print("please reenter a valid coordinate")
			continue	  
		if(check_full_column(coordinate) == 0):     #check if the column is full
			print("Your turn is lost ")
			turn = (turn +1)%num_players       #change checker as the player's turn is lost 
			continue          #repeat loop
		else:
			break     #if and only if correct coordinate is entered-->break loop 

	for row in range(num_rows):     #place coordinate in to the lowest row avaiable
		if(row+1 >= num_rows or board[row+1][coordinate] != "" and board[row][coordinate] == ""):   #1. check if the coordinate is the first to be in the column  if not, 2. check if the next row of the column is not empty  and 3. check if the coordinate is empty --> then place checker  
			board[row][coordinate] = checkers[turn]
			break

	print_board()   #print board after placing checker

	if(check_vertical_win(turn) or check_horizontal_win(turn) or check_diagonal_win1(turn) or check_diagonal_win2(turn) or check_diagonal_win3(turn) or check_diagonal_win4(turn)):  #if one of the win conditions is met --> end game, inform winner
		print(checkers[turn], "won the game!")
		win == True   
		break

	turn = (turn +1)%num_players    #change checkers
	valid_moves -= 1               

if not win:    #if the "win" varibale is still False --> all the win conditions are not met --> tie
	("It's a tie")

		

