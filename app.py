from glob import glob
from msilib import PID_TITLE
from traceback import print_tb
import pygame

colors = {
    "white":(255,255,255),
    "black":(0,0,0),
    "gray":(112,112,112),
    "green":(0,255,0),
    "yellow":(255,255,0)
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
textFont = pygame.font.Font(pygame.font.get_default_font(), 40)

secretWord="NOBRE"
gameOver = False
letters=0
keepPlaying = True

def drawTable():
    global turn
    global table
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen,colors["white"], [col*70+30,row*70+10,50,50],2,5)
            letterText=textFont.render(table[row][col],True,colors["white"])
            screen.blit(letterText, (col*70+39,row*70+18))
    pygame.draw.rect(screen,colors["green"],[15, turn*70+4, width - 40, 63],2,5)

def verifyWord():
    global turn
    global table
    global secretWord
    for col in range(0,5):
        for row in range(0,6):
            if secretWord[col] == table[row][col] and turn > row:
                pygame.draw.rect(screen,colors["green"],[col*70+30,row*70+10,50,50],0,5)
            elif table[row][col] in secretWord and turn > row:
                 pygame.draw.rect(screen,colors["yellow"],[col*70+30,row*70+10,50,50],0,5)

running = True
while running:
    timer.tick(fps)
    screen.fill(colors["gray"])
    verifyWord()
    drawTable()
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                table[turn][letters-1] = " "
                letters -= 1
            if event.key == pygame.K_RETURN and not gameOver:
                turn += 1
                letters = 0

        if event.type== pygame.TEXTINPUT and keepPlaying and not gameOver:
            playerInput = event.__getattribute__("text").upper()
            print(event)
            table[turn][letters] = playerInput
            letters += 1

    for row in range(0,6):
        auxWord = table[row][0]+table[row][1]+table[row][2]+table[row][3]+table[row][4]
        if auxWord == secretWord and row < turn:
            gameOver = True

    if letters == 5:
        keepPlaying = False
    if letters<5:
        keepPlaying = True

    if turn == 6:
        gameOver = True
        loser = textFont.render("You lose!", True, colors["black"])
        screen.blit(loser,(40,600))
    
    if gameOver and turn << 6:
        winner = textFont.render("You Won!", True, colors["black"])
        screen.blit(winner,(40,500))

    pygame.display.flip()
pygame.quit()