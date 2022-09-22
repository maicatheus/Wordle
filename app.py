import pygame

colors = {
    "white":(255,255,255),
    "black":(0,0,0),
    "gray":(112,112,112),
    "green":(0,255,0)
}

pygame.init()

width = 400
height = 600

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Wordle BR")

turn = 0
table =[[" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "]]


fps = 30
timer  = pygame.time.Clock()
boldFont = pygame.font.Font(pygame.font.get_default_font(), 40)

def drawTable():
    global turn
    global table
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen,colors["white"], [col*70+30,row*70+10,50,50],2,3,4)
            letterText=boldFont.render(table[row][col],True,colors["white"])
            screen.blit(letterText, (col*70+39,row*70+18))
    pygame.draw.rect(screen,colors["green"],[15, turn*70+4, width - 40, 63],3,4)

running = True
while running:
    timer.tick(fps)
    screen.fill(colors["gray"])
    drawTable()
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False


    pygame.display.flip()
pygame.quit()