import  pygame
import  sys
import  random
from    agent   import  Agent
import  time

X_TURN  = 1
O_TURN  = 2

X_WIN   = 1
O_WIN   = 2
DRAW    = 3
RUNNING = 4

MINIMAX     = 1
GENETIC     = 2
MONTE_CARLO = 3

class Game :

    def __init__(self):
        self.board = None 
        self.turn = random.choice([X_TURN, O_TURN])
        self.state = RUNNING
        self.opponent = MINIMAX

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
        pygame.draw.line(surface, (255, 0, 0), (128 * x + 10, 128 * y + 10), (128 * x + 128 - 10, 128 * y + 128 - 10), 10)
        pygame.draw.line(surface, (255, 0, 0), (128 * x + 10, 128 * y + 128 - 10), (128 * x + 128 - 10, 128 * y + 10), 10)
        pygame.display.update()

    def draw_O(self, x, y, surface) :
        pygame.draw.circle(surface, (0, 0, 255), (128 * x + 64, 128 * y + 64), 60, 7)
        pygame.display.update()

    def initBoard(self, surface) :
        surface.fill((0, 0, 0))
        self.state = RUNNING
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.opponent = None
        while self.opponent == None :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit("You Exited The Game")
                if event.type == pygame.MOUSEBUTTONDOWN :
                    _, y = pygame.mouse.get_pos()
                    y //= 128
                    if y == 0 :
                        self.opponent = MINIMAX
                    elif y == 1 :
                        self.opponent = GENETIC
                    elif y == 2 :
                        self.opponent = MONTE_CARLO
            font = pygame.font.SysFont("chalkduster", 25)
            textMiniMax    = font.render("MiniMax Algorithm",     False, (0, 255, 0))
            textGenetic    = font.render("Genetic Algorithm",     False, (0, 255, 0))
            textMonteCarlo = font.render("Monte Carlo Algorithm", False, (0, 255, 0))
            surface.blit(textMiniMax,    (55, 0 + 50))
            surface.blit(textGenetic,    (55, 127 + 50))
            surface.blit(textMonteCarlo, (30, 127 * 2 + 50))
            pygame.display.update()
        
        surface.fill((0, 0, 0))
        # Draw The Lines for The board
        pygame.draw.line(surface, (255, 255, 255), (128, 0), (128, 128 * 3), 7)
        pygame.draw.line(surface, (255, 255, 255), (128 * 2, 0), (128 * 2, 128 * 3), 7)
        
        pygame.draw.line(surface, (255, 255, 255), (0, 128), (128 * 3, 128), 7)
        pygame.draw.line(surface, (255, 255, 255), (0, 128 * 2), (128 * 3, 128 * 2), 7)
        
        pygame.display.update()

    def end(self, surface) :
        time.sleep(1)
        font = pygame.font.SysFont("chalkduster", 50)
        text = None
        if self.state == X_WIN :
            text = font.render("You Wine!",  False, (0, 0, 255))
        elif self.state == O_WIN :
            text = font.render("AI Wine!",   False,  (0, 0, 255))
        elif self.state == DRAW :
            text = font.render("Its a draw!", False, (0, 0, 255))
        print("Hello !")
        surface.fill((0, 0, 0))
        surface.blit(text, (50, 127))
        brk = False
        while brk == False :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit("You Exited The Game")
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    brk = True
                    break
            pygame.display.update()

    def run(self) :
        
        pygame.init()
        screen = pygame.display.set_mode((3 * 128, 3 * 128))
        pygame.display.set_caption("Tic Tac Toe")
        
        self.initBoard(screen)
        while True:
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
                x, y = (0, 0)
                time.sleep(0.5)
                if self.opponent == MINIMAX :
                    x, y = Agent.playMiniMax(self)
                elif self.opponent == GENETIC :
                    x, y = Agent.playGenetic(self)
                elif self.opponent == MONTE_CARLO :
                    x, y = Agent.playMonteCarlo(self)
                self.board[y][x] = 'O'
                self.turn = X_TURN
                self.draw_O(x, y, screen)
                self.state = self.eval_board()
            if self.state != RUNNING :
                self.end(screen)
                self.initBoard(screen)