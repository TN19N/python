import math

X_WIN   = 1
O_WIN   = 2
DRAW    = 3
RUNNING = 4

def minimax(game, maximizingPlayer) :
    
    res = game.eval_board()
    if res != RUNNING :
        return {X_WIN:-1, DRAW:0, O_WIN:1}[res]
    
    if (maximizingPlayer) :
        maxScore = -math.inf
        for y in range(3) :
            for x in range(3) :
                if game.board[y][x] == None :
                    game.board[y][x] = 'O'
                    maxScore = max(minimax(game, False), maxScore)
                    game.board[y][x] = None
        return maxScore
    else :
        minScore = math.inf
        for y in range(3) :
            for x in range(3) :
                if game.board[y][x] == None :
                    game.board[y][x] = 'X'
                    minScore = min(minimax(game, True), minScore)
                    game.board[y][x] = None
        return minScore

# Agent Have O Mark
class Agent :
      
    def play(game) :
        bestMove = (0, 0)
        maxScore = -math.inf
        
        for y in range(3) :
            for x in range(3) :
                if game.board[y][x] == None :
                    game.board[y][x] = 'O'
                    score = minimax(game, False)
                    game.board[y][x] = None
                    if score > maxScore :
                        maxScore = score
                        bestMove = (x, y)

        return bestMove