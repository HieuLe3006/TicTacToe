"""
Tic Tac Toe Player
"""

import math
from numpy import inf
import copy

X = "X"
O = "O"
EMPTY = None
count = 0;


def initial_state():
    """
    Returns starting state of the board.
    """
    count = 0;
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Assuming X always goes first -> if number of X on the board is = number of O on the board, then it is X's turn to move
    countX = 0;
    countO = 0;
    for i in range(3):
        for j in range(3):
            if board[i][j] is X:
                countX+=1;
            elif board[i][j] is O:
                countO+=1;
    
    turn = EMPTY;
    if countX == countO:
        turn = X;
    else:
        turn = O;
    return turn; 
        
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    theSet = set(); 
    
    for x in range(3):
        for y in range(3):
            if board[x][y] is EMPTY:  
                action = (x, y);
                # print(action);
                theSet.add(action);
    # print(theSet);
       
    return theSet;
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    newboard = copy.deepcopy(board);                           
       
    x = action[0];
    y = action[1];
    
    # print(newboard);
    # print(action);
    if newboard[x][y] is EMPTY: # Check if action is valid
        newboard[x][y] = player(board);
        
    else:        
        raise ValueError('Action is invalid!');
        
    return newboard;
    
    raise NotImplementedError


# Additional function to check which player is the winner
def checkWinner(board, player):
    if ((board[0][0] is player and board[1][0] is player and board[2][0] is player) 
        or (board[0][2] is player and board[1][2] is player and board[2][2] is player)
        or (board[1][0] is player and board[1][1] is player and board[1][2] is player)
        or (board[0][0] is player and board[0][1] is player and board[0][2] is player)
        or (board[0][0] is player and board[1][1] is player and board[2][2] is player)
        or (board[2][0] is player and board[2][1] is player and board[2][2] is player)
        or (board[0][2] is player and board[1][1] is player and board[2][0] is player)
        or (board[0][1] is player and board[1][1] is player and board[2][1] is player)):
        return 1;
    return 0;

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    player = EMPTY; 
    
    if checkWinner(board, X) == 1:
        player = X;
    elif checkWinner(board, O) == 1:
        player = O;
    
    return player;
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = False;
    
    if winner(board) is not EMPTY:
        win = True;
    
    count = 0;
    for i in range(3):
       for j in range(3):
            if board[i][j] != None:
                count+=1;
        
    if count==9:
        win = True;
    
    return win;
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1;
    elif winner(board) is O:
        return -1;
    else:
        return 0;
    
    raise NotImplementedError

def vertical_lane(board, action, player, opponent):
    x = action[0];
    y = action[1];
    print(x, end = " ");
    print(y);
    print(board);
    print(player);
    print(opponent);
    i = 0;
    counterPlayer = 0; 
    counterOpponent = 0;
    while(i<x):
        print("prior")
        if board[i][y] is opponent:
            print("eks 0")
            counterOpponent+=1;
        if board[i][y] is player: 
            counterPlayer+=1;
            print("hju0");
        i+=1;
    
    i = 2;
    while(i>x):
        print("latter")
        if board[i][y] is opponent:
            print("eks")
            counterOpponent+=1;
        if board[i][y] is player: 
            print("hjiu")
            counterPlayer+=1;
        i-=1;
   
    print("vertical:", end = " "); 
    print(counterPlayer, end = " ");
    print(counterOpponent);    
    if counterPlayer == 1 and counterOpponent == 1: 
        return -2;
    elif counterOpponent == 2 and counterPlayer == 0:
        return -10;
    elif counterOpponent == 0 and counterPlayer == 0:
        return -1; 
    elif counterOpponent == 0 and counterPlayer == 2:
        return -20; 
    else: 
        return 0;
    raise NotImplementedError

def horizontal_lane(board, action, player, opponent):
    x = action[0];
    y = action[1];
    
    i = 0;
    counterPlayer = 0; 
    counterOpponent = 0;
    while(i<y):
        if board[x][i] is opponent:
            counterOpponent+=1;
        if board[x][i] is player: 
            counterPlayer+=1;
        i+=1;
    
    i = 2;
    while(i>y):
        if board[x][i] is opponent:
            counterOpponent+=1;
        if board[x][i] is player: 
            counterPlayer+=1;
        i-=1;
     
    print("horizontal:", end = " ");
    print(counterPlayer, end = " ");
    print(counterOpponent);        
    if counterPlayer == 1 and counterOpponent == 1: 
        return -2;
    elif counterOpponent == 2 and counterPlayer == 0:
        return -10;
    elif counterOpponent == 0 and counterPlayer == 0:
        return -1; 
    elif counterOpponent == 0 and counterPlayer == 2:
        return -20;
    else:
        return 0;
    raise NotImplementedError

def diagonal_lane_left(board, action, player, opponent):
    x = action[0];
    y = action[1];
    
    i = 0;
    j = 0;
    counterPlayer = 0; 
    counterOpponent = 0;
    while(i<x and j<y):
        if board[i][j] is opponent:
            counterOpponent+=1;
        if board[i][j] is player: 
            counterPlayer+=1;
        i+=1;
        j+=1;
    
    i = 2;
    j = 2;
    while(i>x):
        if board[i][j] is opponent:
            counterOpponent+=1;
        if board[i][j] is player: 
            counterPlayer+=1;
        i-=1;
        j-=1;
   
    print("diag left:", end = " ");
    print(counterPlayer, end = " ");
    print(counterOpponent);         
    if counterPlayer == 1 and counterOpponent == 1: 
        return -2;
    elif counterOpponent == 2 and counterPlayer == 0:
        return -10;
    elif counterOpponent == 0 and counterPlayer == 0:
        return -1; 
    elif counterOpponent == 0 and counterPlayer == 2:
        return -20;
    else: 
        return 0;
    raise NotImplementedError

def diagonal_lane_right(board, action, player, opponent):
    x = action[0];
    y = action[1];
    
    i = 0;
    j = 2;
    counterPlayer = 0; 
    counterOpponent = 0;
    while(i<x and j>y):
        if board[i][j] is opponent:
            counterOpponent+=1;
        if board[i][j] is player: 
            counterPlayer+=1;
        i+=1;
        j-=1;
    
    i = 2;
    j = 0;
    while(i>x and j<y):
        if board[i][j] is opponent:
            counterOpponent+=1;
        if board[i][j] is player: 
            counterPlayer+=1;
        i-=1;
        j+=1;
    
    print("diag right:", end = " ");
    print(counterPlayer, end = " ");
    print(counterOpponent);        
    if counterPlayer == 1 and counterOpponent == 1: 
        return -2;
    elif counterOpponent == 2 and counterPlayer == 0:
        return -10;
    elif counterOpponent == 0 and counterPlayer == 0:
        return -1; 
    elif counterOpponent == 0 and counterPlayer == 2:
        return -20;
    else: 
        return 0;
    raise NotImplementedError

def diagonal_lane(board, action, player, opponent):
    x = action[0];
    y = action[1];
    
    score = 0;
    
    if x==1 and y==1:
        score = diagonal_lane_left(board, action, player, opponent) + diagonal_lane_right(board, action, player, opponent);
    elif ((x==0 and y==0) or (x==2 and y==2)):
        score = diagonal_lane_left(board, action, player, opponent);
    else:
        score = diagonal_lane_right(board, action, player, opponent);
        
    
    return score;

    raise NotImplementedError;


# Func to evaluate node
def evaluate(board, player, action):
    # considers 3 lanes: diagonal, vertial, and horizontal lanes
    # if 3 positions in a lane have none of the opponent's moves -> +1 for max value and -1 for min value
    # every opponent move on a lane -> -1 for min value (only if the there's no player's move on the lane)
    # if there are 2 opponent moves in a lane -> value turns into -10
    x = action[0];
    y = action[1];
    vertical_score = 0;
    diagonal_score = 0;
    horizontal_score = 0;       
    print("player: ", end = " ");
    print(player, end = " ");
    if player is O: 
        opponent = X;
        print("opponent: ", end = " ");
        print(opponent);
        # Considering 4 nodes/slots that don't contribute to the winning condition of diagonal lanes
        if ((x==0 and y==1) or (x==1 and y==0) or (x==1 and y==2) or (x==2 and y==1)):
            vertical_score = vertical_lane(board, action, player, opponent);
            horizontal_score = horizontal_lane(board, action, player, opponent);
            score = vertical_score + horizontal_score;
            return score;
        else:     
            vertical_score = vertical_lane(board, action, player, opponent);
            horizontal_score = horizontal_lane(board, action, player, opponent);
            diagonal_score = diagonal_lane(board, action, player, opponent);
            score = vertical_score + horizontal_score + diagonal_score;
            return score;
    else:
        opponent = O;
        print("opponent: ", end = " ");
        print(opponent);
        if ((x==0 and y==1) or (x==1 and y==0) or (x==1 and y==2) or (x==2 and y==1)):
            vertical_score = vertical_lane(board, action, player, opponent);
            horizontal_score = horizontal_lane(board, action, player, opponent);
            score = vertical_score + horizontal_score;
            print(vertical_score, end = " ");
            print(horizontal_score);
            return score;
        else:     
            vertical_score = vertical_lane(board, action, player, opponent);
            horizontal_score = horizontal_lane(board, action, player, opponent);
            diagonal_score = diagonal_lane(board, action, player, opponent);
            score = vertical_score + horizontal_score + diagonal_score;
            return score;
    
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("---------------------------");
    if terminal(board) == True:
        return None;
    else:
        theplayer = player(board);
        # print(theplayer);
        theaction = (0, 0);
        if theplayer is X: # if player is X - the one who goes first) -> minimax
            value = float(-inf);
            for action in actions(board):
                # print(action);
                newvalue = abs(evaluate(board, theplayer, action));
                print(action, end = " ");
                print(newvalue);
                if value<newvalue:
                    value = newvalue;
                    theaction = action;
                # print(newvalue);
        else:
            print("adsfasdf");
            value = float(+inf);
            for action in actions(board):
                # print(action);
                newvalue = evaluate(board, theplayer, action);
                print(action, end = " ");
                print(newvalue);
                if value>newvalue:
                    value = newvalue;
                    theaction = action;
                # print(newvalue);
        
        print(theaction);    
        return theaction;
    
    raise NotImplementedError
