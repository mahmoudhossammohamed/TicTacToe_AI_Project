from operator import truediv

# key and value
board = {1:' ', 2:' ' , 3:' ' ,
         4:' ', 5:' ' , 6:' ' ,
         7:' ', 8:' ' , 9:' ' }

#the shape of the board
def printBoard(board):
    print('| '+board[1] + ' | ' + board[2] + ' | ' + board[3]+' |')
    print('| '+board[4] + ' | ' + board[5] + ' | ' + board[6]+' |')
    print('| '+board[7] + ' | ' + board[8] + ' | ' + board[9]+' |')
    print("-------------")
#printBoard(board)

#chek is the this position is free or not
def spaceIsFree(position):
    if(board[position] == ' '):
        return True
    else: 
        return False
#print(spaceIsFree(2))
#print(spaceIsFree(1))
#print(spaceIsFree(4))            

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position]=letter
        printBoard(board)
        if checkForWin():
            if letter == 'O': # O--> the computer wins
                print('You lose! (Try again)')
                input("Enter any number to exit!")
                exit()
            else:
                print('You win! (Congratulations)')
                input("Enter any number to exit!")

                exit()
        if (checkDraw()):
            print('Draw!')
            input("Enter any number to exit!")
            exit()

                        

    else:
        print('cannot play here!!')
        position = int(input("Enter the new position: "))
        insertLetter(letter, position)
        return    
#insertLetter("X" ,2 )
#insertLetter("X" ,5 )
#insertLetter("X" ,6 )
#insertLetter("X" ,2 )

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
            #if there is empty fields, so we can still play
    return True    

def checkForWin():
    if (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True                                    
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
        return True 
    else:
        return False

player = 'ْX'
bot = 'O'
def playerMove():
    position = int (input("Enter the position for 'X': "))
    insertLetter(player, position)
    return
"""
def computerMove():
    position = int (input("Enter the position for 'O': "))
    insertLetter(bot, position)
    return        

while not checkForWin():
    computerMove()    
    playerMove()
"""
def computerMove():
    bestScore = -1
    bestMove = 0

    for key in board.keys():
        if (board[key]==' '):
            board[key] = bot
            score = miniMax(board, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)
    return

def miniMax(board, isMaximizing):
    if checkWhichMarkWin(bot):
        return 1
    elif checkWhichMarkWin(player):
        return -1
    elif checkDraw():
        return 0
        # these lower two functions still works and then we go to the upper three cases to work
    if isMaximizing: # maximizing   ###bot
        bestScore = -1
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = miniMax(board, False) #this false for minimizing
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score    
        return bestScore

    else:    #minimizing           ###player
        bestScore = 1
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = miniMax(board, True) #this True for maximizing
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score    
        return bestScore





#used in minimax in knowing which mark has one 
def checkWhichMarkWin(mark):
    if (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True                                    
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] == mark):
        return True 
    else:
        return False    

print("Positions are as follow:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print("You can start with the first step")
while not checkForWin():
    playerMove()        
    computerMove()    
    #playerMove()        