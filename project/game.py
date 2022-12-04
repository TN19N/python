import  pygame
import  sys
import  random
from    agent   import  Agent

X_TURN  = 1
O_TURN  = 2

X_WIN   = 1
O_WIN   = 2
DRAW    = 3
RUNNING = 4

class Game :
    
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.turn = random.choice([X_TURN, O_TURN])
        self.state = RUNNING
    
    def eval_board(self) :
        
        for y in range(3) :
            if self.board[y][0] == self.board[y][1] == self.board[y][2] != None :
                return X_WIN if self.board[y][0] == 'X' else O_WIN

        for x in range(3) :
            if self.board[0][x] == self.board[1][x] == self.board[2][x] != None:
                return X_WIN if self.board[0][x] == 'X' else O_WIN

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None :
            return X_WIN if self.board[0][0] == 'X' else O_WIN
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None :
            return X_WIN if self.board[0][2] == 'X' else O_WIN

        for y in range(3) :
            for x in range(3) :
                if self.board[y][x] == None :
                    return RUNNING
        return DRAW
    
    def draw_x(self, x, y, surface) :
        pygame.draw.line(surface, (192, 192, 192), (128 * x + 10, 128 * y + 10), (128 * x + 128 - 10, 128 * y + 128 - 10), 10)
        pygame.draw.line(surface, (192, 192, 192), (128 * x + 10, 128 * y + 128 - 10), (128 * x + 128 - 10, 128 * y + 10), 10)
        
    def draw_O(self, x, y, surface) :
        pygame.draw.circle(surface, (192, 192, 192), (128 * x + 64, 128 * y + 64), 60, 7)
        
    def initBoard(self, surface) :
        surface.fill((0, 0, 0))
                
        # Draw The Lines for The board
        pygame.draw.line(surface, (255, 255, 255), (128, 0), (128, 128 * 3), 7)
        pygame.draw.line(surface, (255, 255, 255), (128 * 2, 0), (128 * 2, 128 * 3), 7)
        
        pygame.draw.line(surface, (255, 255, 255), (0, 128), (128 * 3, 128), 7)
        pygame.draw.line(surface, (255, 255, 255), (0, 128 * 2), (128 * 3, 128 * 2), 7)
        
        pygame.display.update()
        
    def run(self) :
        
        pygame.init()
        screen = pygame.display.set_mode((3 * 128, 3 * 128))
        pygame.display.set_caption("Tic Tac Toe")
        
        self.initBoard(screen)
        while self.state == RUNNING:

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit("You Exited The Game")
                elif event.type == pygame.MOUSEBUTTONDOWN and self.turn == X_TURN :
                    x, y = pygame.mouse.get_pos()
                    x //= 128
                    y //= 128
                    if self.board[y][x] == None :
                        self.board[y][x] = 'X'
                        self.turn = O_TURN
                        self.draw_x(x, y, screen)
                        self.state = self.eval_board()

            if self.state == RUNNING and self.turn == O_TURN :
                x, y = Agent.play(self)
                self.board[y][x] = 'O'
                self.turn = X_TURN
                self.draw_O(x, y, screen)
                self.state = self.eval_board()

            pygame.display.update()

        if self.state == X_WIN :
            print("You Wine!")
        elif self.state == O_WIN :
            print("AI Wine")
        elif self.state == DRAW :
            print("Its A draw")

        pygame.quit()