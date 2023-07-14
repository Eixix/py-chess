# import pygame
from Chessboard import Chessboard

chessboard = Chessboard()

figure = chessboard.get_figure_from_position((3, 3))

if figure is not None:
    print(figure)
    print(figure.get_moves((3, 3), chessboard))

# pygame.init()

# SIZE = 100

# screen = pygame.display.set_mode((SIZE * 8, SIZE * 8))

# running = True

# clock = pygame.time.Clock()

# chessboard = Chessboard()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))

#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()
