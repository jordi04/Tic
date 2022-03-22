import colorama
import sys, pygame
pygame.init()

size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255
purple = 150, 0, 75

X = 300
Y = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption("MasterMind")

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("MasterMind", True, white, purple)

textRect = text.get_rect()
textRect.center = (X, Y)

run = True
actual_input = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.K_0: 
            actual_input.append(0)
        if event.type == pygame.K_1: 
            actual_input.append(1)
        if event.type == pygame.K_2: 
            actual_input.append(2)
        if event.type == pygame.K_3: 
            actual_input.append(3)
        if event.type == pygame.K_4: 
            actual_input.append(4)
        if event.type == pygame.K_5: 
            actual_input.append(5)
        if event.type == pygame.K_6: 
            actual_input.append(6)
        if event.type == pygame.K_7: 
            actual_input.append(7)
        if event.type == pygame.K_8: 
            actual_input.append(8)
        if event.type == pygame.K_9: 
            actual_input.append(9)
        else:
            pass

    
    screen.fill(purple)
    screen.blit(text, textRect)

    pygame.display.flip()