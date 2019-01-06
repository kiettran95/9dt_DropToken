'''
9dt.py 
98point6 Drop Token
Kiet Tran
06/01/2019

'''

class DropToken:
    '''
    Defines API for 9dt - Drop Token Game
    To process new command, use execute function and pass the whole command string

    '''

    def __init__(self):
        '''
        Initialize:
            Default player 1 goes first
            Rows score
            Columns score
            Diagonals score
            Game exit status
            Winner
            Succesfully columns put to
            Board
        '''

        self.player = 1                         #default starting with player 1
        self.rows = [0,0,0,0]                   #filled rows score
        self.columns = [0,0,0,0]                #filled columns score
        self.diagonals = [0,0]                  #filled diagonals score
        self.status = 0                         #game exit status
        self.winner = 0                         #win status
        self.tokens = []                        #filled tokens
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]      #starting board


    # process new command
    def execute(self, command):
        '''
        Parses all commands
        Verifies command correctness
        Executes the required command
        Prints informational error messages
        
        INPUT: The whole command string
        OUTPUT: 1, 0, or -1:
            Return 1: OK
            Return 0: Valid format but failed execution
            Return -1: Invalid format.
        '''
        
        inputs = command.lower().split( )

        if len(inputs) == 2 or len(inputs) == 1:                 #there is a command

            if inputs[0] == 'put':              #PUT command

                if len(inputs) != 2:            #invalid PUT command
                    print('ERROR')
                    return -1

                try:
                    col = int(inputs[1])        #get column
                    if col < 1 or col > 4:      #invalid column
                        raise ValueError

                except ValueError:
                    print('ERROR')              #invalid format
                    return -1

                else:
                    if self._put(col):           #if put is successfully

                        if self.winner != 0:        #if there is a winner
                            print('WIN')
                            return 1

                        elif self.isDraw():     #game is draw
                            print('DRAW')
                            return 1

                        else:                   #game is continue
                            print('OK')
                            return 1

                    else:
                        print('ERROR')          #put is fail
                        return 0

            elif inputs[0] == 'get':            #GET command
                self.get()
                return 1

            elif inputs[0] == 'board':          #BOARD command
                self.printBoard()
                return 1

            elif inputs[0] == 'exit':           #EXIT command
                self.exit()
                return 1

            else:                               #invalid command
                print('ERROR')
                return -1

        else:
            print('ERROR')                      #invalid input 
            return -1


    # validate win state
    def isWin(self, row, col):
        '''
        Helper function to determine the win state
        
        INPUT: 
            Row to check
            Column to check
        OUTPUT: 1, 0:
            Return 1: Win-OK
            Return 0: No winner
        '''
        if (abs(self.rows[row]) == 4            #if the whole row is filled by one player
            or abs(self.columns[col]) == 4      #if the whole column is filled by one player
            or abs(self.diagonals[0]) == 4      #if the diagonal is filled by one player
            or abs(self.diagonals[1]) == 4):    #if the anti-diagonal is filled by one player
            
            self.winner = self.player
            return 1

        return 0        #reached here if there is no winner 


    # validate draw state
    def isDraw(self):
        '''
        Helper function to determine the draw state
    
        OUTPUT: 1, 0:
            Return 1: DRAW-OK
            Return 0: Game is continue
        '''
        if len(self.tokens) == 16:              #the board is full
            return 1

        return 0        #game is not over


    # put into column
    def _put(self, col):
        '''
        Helper function to process put token into column of the board
        Starts with first available row from bottom to drop token in current column
        
        INPUT:
            Column to put to
        OUTPUT: 1 or 0:
            Return 1: OK-Success
            Return 0: Fail-Current column is filled
        '''
        if col < 1 or col > 4 or col != int(col):     #ishould not happen under normal circumstances
            return 0

        if self.winner != 0:                    #if there is already a winner
            return 0

        col -= 1                                
        val = 1 if self.player == 1 else -1     #value used to keep track game status
        size = len(self.rows)                   #size of rows

        for row in range(3,-1,-1):
            
            if self.board[row][col] == 0:
                
                self.board[row][col] = self.player       #update board

                self.rows[row] += val                    #update rows

                self.columns[col] += val                    #update cols

                if col == row:                  #the spot is on diagonal
                    self.diagonals[0] += val

                if col + row == size - 1:           #the spot is on anti-diagonal
                    self.diagonals[1] += val

                self.isWin(row, col)
                
                self.player = (self.player % 2) + 1

                self.tokens.append(col + 1)
                return 1


        return 0            #reach here if the current column is not available


    # get valid input history
    def get(self):
        '''
        Prints succesfully processed columns history

        '''
        for col in self.tokens:                 #print all filled columns history
            print(col)


    # print current board state
    def printBoard(self):
        '''
        Prints the board in a default format

        '''

        for x in self.board:
            print('| ', end ='')
            print(*x, sep=" ")
        print('+--------')
        print('  1 2 3 4')


    # exit game
    def exit(self):
        '''
        Set exit status for current game

        '''

        self.status = 1


    # validate game status
    def isExit(self):
        '''
        Validate if the game is not over

        OUTPUT: True or False:
            Return True: if game is over
            Return False: if game is continue
        '''

        return self.status == 1



if __name__ == '__main__':
    print('')
    print('===================================')
    print(' Welcome to 9dt Drop Token Game!!!')
    print('---- Let\'s have a great time ---')
    print('===================================')
    print('')

    print('Please input with format PUT <column>, GET, BOARD, or EXIT')
    print('')
    print('Starting with player 1...')
    print('')

    game = DropToken()

    while not game.isExit():
        game.execute(input('> '))