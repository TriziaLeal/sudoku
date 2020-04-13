def menu():
	print("----------Menu-----------")
	print ("WELCOME TO SUDOKU!")
	print ("[1] Play Game")
	print ("[2] Instructions")
	print ("[3] Exit")

def instruction():
	print("-----Instructions--------")
	print ("Fill all empty cells so \n that the numbers 1 to 9 \nappear exactly once in\n each row, column and \n3x3 box.")
	print ("How to:")
	print ("1. Input the row,column,\n and square number\n to access cell.")
	print ("2. Input your answer.")
	print()
	print("If you wish to change\n answer, do 1 and 2.")
	print("You can look up the\n Reference Board to know\n which cells are\n changeable.")
	print()
	print("TO QUIT- ENTER '0'")
	print("**Quiting does not \nsave game progress.")
	print("-------------------------")

def randomized():							
	import random																					
	randomNumber = random.randint(1,10)
	return randomNumber

def show_board(sudoku_problem,board):														#prints board  
	print("-------------------------")
	print(board)
	print()
	for row_list in range (len(sudoku_problem)):
		row=sudoku_problem[row_list]
		if row_list==1  or row_list==4 or row_list==7:
			print()
		for col in range(len (row)):
			if col==0 or col==3 or col==6:
				print(row[col]," ", end=" ")
			else:
				print(row[col],end=" ")
		print()
	
	print("-------------------------")

def load_problem(problem_file):																		#access problem in file 
	loadHandle=open(problem_file,"r")
	board_list=[]

	for line in loadHandle:
		row=line[:-1].split(".")
		board_list.append(row)
	loadHandle.close()
	
	return board_list

def check_blank(sudoku_problem):																#check if may blank pa 
	blankcells=0
	for row_list in range (len(sudoku_problem)):
		row=sudoku_problem[row_list]
		for col in range(len (row)):
			if row[col]=="-":
				blankcells+=1																					#counter ng blanks
	return blankcells

def get_row(rownum,problem_file):																#access row input by the user 
	row_checker=problem_file[rownum]
	return row_checker[1:]																				#returns a list containing elements in row

def get_column(colnum,problem_file):															#access column input by the user
	col_checker=[]
	for row_list in range (len(problem_file)):
		col_checker.append(problem_file[row_list][colnum])									#appends elements of column 
	return col_checker[1:]																					#returns a list containing elements in row

def get_square(rownum,colnum,problem_file):
	if rownum<=3 and colnum<= 3:
		square =problem_file[1][1:4]+problem_file[2][1:4]+problem_file[3][1:4]
	
	if rownum<=3 and 4<=colnum<=6:
		square =problem_file[1][4:7]+problem_file[2][4:7]+problem_file[3][4:7]
	
	if rownum<=3 and 7<=colnum<=9:
		square =problem_file[1][7:10]+problem_file[2][7:10]+problem_file[3][7:10]
	
	if 4<=rownum<=6 and colnum<= 3:
		square =problem_file[4][1:4]+problem_file[5][1:4]+problem_file[6][1:4]
	
	if 4<=rownum<=6  and 4<=colnum<=6:
		square =problem_file[4][4:7]+problem_file[5][4:7]+problem_file[6][4:7]
	
	if 4<=rownum<=6 and 7<=colnum<=9:
		square =problem_file[4][7:10]+problem_file[5][7:10]+problem_file[6][7:10]
	
	if 7<=rownum<=9  and colnum<= 3:
		square =problem_file[7][1:4]+problem_file[8][1:4]+problem_file[9][1:4]
	
	if 7<=rownum<=9 and 4<=colnum<=6:
		square =problem_file[7][4:7]+problem_file[8][4:7]+problem_file[9][4:7]
	
	if 7<=rownum<=9 and 7<=colnum<=9:
		square =problem_file[7][7:10]+problem_file[8][7:10]+problem_file[9][7:10]
	return square																								#returns a list containing elements in square

def checker(check_list,answer):																		#check if input exist in list
	for cell in check_list:
		if cell==answer:
			return False																					
	return True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
choice=0
while choice != 3:																				#loop for menu 
	menu()
	choice=int(input("Choose a number:"))
	if choice==1:															
		file_number=randomized()															#chooses problem
		if file_number==1:
			problem_file="problem_1.txt"
		if file_number==2:
			problem_file="problem_2.txt"
		if file_number==3:
			problem_file="problem_3.txt"
		if file_number==4:
			problem_file="problem_4.txt"
		if file_number==5:
			problem_file="problem_5.txt"
		if file_number==6:
			problem_file="problem_6.txt"
		if file_number==7:
			problem_file="problem_7.txt"
		if file_number==8:
			problem_file="problem_8.txt"
		if file_number==9:
			problem_file="problem_9.txt"
		if file_number==10:
			problem_file="problem_10.txt"
		
		original_board=load_problem(problem_file)									#list contains original problem
		record_answer=load_problem(problem_file)									#list contains problem w/ user's answer
		number_blank=check_blank(record_answer)
		rownum=""
		colnum=""
		squarenum=""
		answer=""
				
		while number_blank != 0:															#loop while problem is not solved	

			show_board(original_board,"REFERENCE BOARD")						#prints original board
			show_board(record_answer,"PLAYING BOARD")						#prints board with answers
			print("TO QUIT- ENTER '0'")
			print("**Quiting does not save\n your progress.")
						
			rownum=int(input("ENTER ROW NUMBER:"))
			if rownum>9:
				print("Invalid! ")
				continue
			if rownum==0:
				break
				
			colnum=int(input("ENTER COLUMN NUMBER:"))
			if colnum>9:
				print("Invalid!")
				continue
			if colnum==0:
				break 
				

			if original_board[rownum][colnum]=="-":
			
				answer=input("ENTER ANSWER:")
				if int(answer)>9:
					print("Invalid!")
					print("")
					continue
				if answer==0:
					break
			
				row_list=get_row(rownum,record_answer)
				column_list=get_column(colnum,record_answer)
				square_list=get_square(rownum,colnum,record_answer)

				row_check=checker(row_list,answer)
				column_check=checker(column_list,answer)
				square_check=checker(square_list,answer)

				if row_check==False:
					print("Wrong! \nInput repeats in row.")
				if column_check==False:
					print("Wrong! \nInput repeats in column.")
				if square_check==False:
					print("Wrong! \nInput repeats in square")
				if row_check==True and column_check==True and square_check==True:
					record_answer[rownum][colnum]=answer
					number_blank-=1
					
			else:
				print("Invalid!")
				print("Cell contains number \ngiven by the board.")
				print("See the Reference\n Board to know which\n cells are changeable.")
			
	if choice==2:
		instruction()

#Jevas Leen Quejada
#www.mathsphere.co.uk
