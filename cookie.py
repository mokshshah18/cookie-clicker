# Importing
import pygame
import time
import math
 
# initiatizing
pygame.init()
#screen variables
""" screen = pygame.display.set_mode() # Default to screen resolution.
area = screen.get_rect()
print(area) """
screen = pygame.display.set_mode((800,800))
screen.fill((255, 255, 255))

#design variables
pygame.display.set_caption('cookie clicker')
font = pygame.font.Font('freesansbold.ttf', 32)

#game variables
score = 10
running = True
cramperBrought = {
    "granny" : 0,
} #amount of bots bought key is the diffrent bots availbile and values are the amount bought
cookieCounterG = 0
while running:

    #game shapes and colliders
    granny = pygame.Rect(600,600,100,100)


    scorep = "Cookies = " + str(score) 
    ScoreText = font.render(scorep,True,(10,10,10))
    Instructions = ["Get to 10 cookies to start automating","welcome to automation land"]
    if(score<10):                                                         
        InstructionText = font.render(Instructions[0],True,(0,0,0))
    else:
        InstructionText = font.render(Instructions[1],True,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#right mouse button events
            #msx, msy get mouse pointer variables
            mouse_x, mouse_y = pygame.mouse.get_pos()
            msx,msy = mouse_x,mouse_y
            if(msx<500 and msx>300 and msy>300 and msy<500):#circle hitbox?
                score += 1
            if(score>10 and granny.collidepoint(msx,msy)):                                            
                cramperBrought["granny"] += 1
                score -= 5
                start_time = time.time()
    
    cookiecounttemp = cookieCounterG
    if (cramperBrought.get("granny")!=0):
        #print(time.time()-start_time,cramperBrought["granny"])
        cookieCounterG = math.floor(time.time()-start_time) * cramperBrought["granny"]
        print(cookieCounterG)
        if(cookieCounterG>cookiecounttemp):
            score += cramperBrought["granny"]
    #drawing
    pygame.draw.circle(screen, (0,0,100), (400, 400), 100, 100)
    screen.blit(ScoreText,(10,10))#displays text
    screen.blit(InstructionText,(70,600))
    if(score>10):
        pygame.draw.rect(screen,(0,0,0),granny)
    #update
    pygame.display.update()
    #clean screen
    screen.fill((255, 255, 255))