import pygame

import ChessEngine
import Move
WIDTH = HEIGHT = 600

ROWS = COLS = DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["wp", "wr", "wn", "wb", "wk", "wq", "bp", "br", "bn", "bb", "bk", "bq"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()

                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                print(col, row)
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                    print(playerClicks)
                if len(playerClicks) == 2:
                    move = Move.Move(playerClicks[0], playerClicks[1], gs.board)

                    print(move.getChessNotation())

                    gs.makeMove(move)

                    sqSelected = ()

                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawBoard(screen):
    color_bg = [pygame.Color("white"), pygame.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = color_bg[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


if __name__ == "__main__":
    main()
