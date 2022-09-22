import pygame

colors = {
    "white":(255,255,255),
    "black":(0,0,0)
}

pygame.init()

width = 400
height = 600

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Wordle BR")

fps = 30
timer  = pygame.time.Clock()

running = True
while running:
    timer.tick(fps)
    screen.fill(colors["black"])

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False


    pygame.display.flip()
pygame.quit()