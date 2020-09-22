def draw_board(the_board):
    import pygame
    """ Draw a chess board with queens, from the_board. """
    surface_sz = 480           # Proposed physical surface size.
    colors = [(255, 0, 0), (0, 0, 0)]
    ball = pygame.image.load("ball.png")

    pygame.init()

    n = len(the_board)
    cell_sz = 480 // n
    surface_sz = cell_sz * n

    board = pygame.display.set_mode((surface_sz, surface_sz))
    cell = (10, 10, cell_sz, cell_sz)

    for i in range(n):
        for j in range(n):
            cell = (i * cell_sz, j * cell_sz ,cell_sz, cell_sz)
            board.fill(colors[(i + j) % 2], cell)

    # ball.width = cell_sz * 0.8    # так не работает
    for (col, row) in enumerate(the_board):
    # draw a queen at col, row...
        board.blit(ball, (col * cell_sz, row * cell_sz))

    return board
