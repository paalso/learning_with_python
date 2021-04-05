import pygame
import draw_queens


def main():
    FPS = 10
    clock = pygame.time.Clock()

    the_board = [6,4,2,0,5,7,1,3]
    board = draw_queens.draw_board(the_board)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
