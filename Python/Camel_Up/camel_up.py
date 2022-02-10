import sys, pygame
pygame.init()

size = width, height = 800, 500
background = 100, 50, 100
color_light = 255, 100, 100
color_dark = 100, 50, 0
run = True
color = (255,255,255)

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , True , color)

screen = pygame.display.set_mode(size)

screen.fill(background)

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                
    pygame.draw.line(screen, (255, 255, 255), (500, 450), (0, 450))

    mouse = pygame.mouse.get_pos()
     # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
      
    # superimposing the text onto our button
    screen.blit(text , (width/2+50,height/2))
    pygame.display.flip()
    

    