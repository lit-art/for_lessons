import pygame

pygame.init()
size = [960, 540]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Родненький свой любимiй курсор")
done = False
clock = pygame.time.Clock()

Cursor = pygame.image.load('arrow.png')


def draw_cursor(screen, x, y):
    screen.blit(Cursor, (x, y - 48))


pygame.mouse.set_visible(0)
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    draw_cursor(screen, x, y)

    pygame.display.flip()

    clock.tick(20)
