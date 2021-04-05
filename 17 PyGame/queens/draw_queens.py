import pygame


def draw_board(
        the_board, surface_sz=480,
        colors=[(0, 0, 0), (255, 0, 0)]):
    """ Draw a chess board with queens, from the_board.
        Returns a surface with a chess board drawn on it """

    board_size = len(the_board)
    cell_sz = surface_sz // board_size
    adjusted_sz = cell_sz * board_size

    pygame.init()
    surface = pygame.display.set_mode((adjusted_sz, adjusted_sz))

    # Bottom right cell color = colors[0]
    start_color_id = 0 if board_size % 2 else 1
    for x in range(board_size):
        for y in range(board_size):
            color_id = (start_color_id + x + y) % 2
            pygame.draw.rect(surface, colors[color_id],
                    (x * cell_sz, y * cell_sz, cell_sz, cell_sz))

    # Now that squares are drawn, draw the queens.

    return surface
