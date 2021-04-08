import pygame

from colors import DARK_RED, LIGHT_YELLOW

def draw_board(
        the_board, surface_sz=600,
        colors=[DARK_RED, LIGHT_YELLOW]):
    """ Draw a chess board with queens, from the_board"""

    FPS = 10
    clock = pygame.time.Clock()

    board_size = len(the_board)
    cell_sz = surface_sz // board_size
    adjusted_sz = cell_sz * board_size

    pygame.init()
    surface = pygame.display.set_mode((adjusted_sz, adjusted_sz))

    queen = pygame.image.load("img/queen.png")
    queen = pygame.transform.scale(queen,
            (int(0.8 * cell_sz) , int(0.8 * cell_sz )))

    # Draw the blank board
    # Bottom right cell color = colors[0]
    start_color_id = 0 if board_size % 2 else 1
    for x in range(board_size):
        for y in range(board_size):
            color_id = (start_color_id + x + y) % 2
            pygame.draw.rect(surface, colors[color_id],
                    (x * cell_sz, y * cell_sz, cell_sz, cell_sz))

        # Draw the Queens on tha board
        queen_rect = queen.get_rect(
                center=((x + 0.5) * cell_sz, (the_board[x] + 0.5) * cell_sz))
        surface.blit(queen, queen_rect)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()
