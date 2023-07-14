# import pygame

from Chessboard import Chessboard

chessboard = Chessboard()
figure = chessboard.get_figure_from_position((4, 3))
print("Figure: " + str(figure))
print(figure.get_moves((4, 3), chessboard))

# pygame.init()
#
# size = 100
#
# screen = pygame.display.set_mode((size * 8, size * 8))
#
# running = True
#
# clock = pygame.time.Clock()
# chessboard = Chessboard()
#
#
# def draw_board() -> None:
#     pass
#
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))
#     draw_board()
#
#     pygame.display.flip()
#
#     clock.tick(60)
#
# pygame.quit()
