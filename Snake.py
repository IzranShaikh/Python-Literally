#importing modules
import pygame
import time
import random
from colors import *

#initialzing pygame
pygame.init()

#texture hardcoding
d_width=1100
d_height=650
block_size = 10

#creating display/window
game_screen=pygame.display.set_mode((d_width,d_height))

#game title
pygame.display.set_caption('Snake!!')

#setting icon
icon = pygame.image.load('i_snake_t.png')
pygame.display.set_icon(icon)

#fps
fps_change=10

font=pygame.font.SysFont('Ninja Naruto',20)

#message function
def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    game_screen.blit(screen_text,[420,d_height/2])

#snake
def snake(block_size,snakelist):
    for x_y in snakelist:
        pygame.draw.rect(game_screen,aqua,[x_y[0],x_y[1],block_size,block_size])

#var for fps
fps = pygame.time.Clock()

#main loop
def gameLoop():

    #exit/run
    game_exit = False
    gameOver = False

    #important variables
    head_x=round((d_width/2)/10.0)*10.0
    head_x_change=0
    head_y=round((d_height/2)/10.0)*10.0
    head_y_change=0

    #snakelist
    snakelist = []
    snakelength=1

    #apple variables
    apple_x = round(random.randrange(12,1080-block_size)/10.0)*10.0
    apple_y = round(random.randrange(10,635-block_size)/10.0)*10.0

    while not game_exit:

        while gameOver==True:
            game_screen.fill(white)
            message_to_screen('Game over,Press P to play again OR X to exit',emeraldgreen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        game_exit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameLoop()

        #event handling for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            #movement controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    head_x_change += block_size
                    head_y_change = 0
                elif event.key == pygame.K_LEFT:
                    head_x_change -= block_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change -= block_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change += block_size
                    head_x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    head_x_change = block_size
                    head_y_change = 0
                elif event.key == pygame.K_LEFT:
                    head_x_change = -block_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -block_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = block_size
                    head_x_change = 0

        if head_x > 1080 or head_x <= 4 or head_y > 630 or head_y <= 4:
            gameOver = True

        #changes
        head_x += head_x_change
        head_y += head_y_change

        #background
        game_screen.fill(white)

        ##########game screen##########

        #borders
        pygame.draw.line(game_screen,red1,(5,5),(1090,5))
        pygame.draw.line(game_screen,red1,(1090,5),(1090,640))
        pygame.draw.line(game_screen,red1,(1090,640),(5,640))
        pygame.draw.line(game_screen,red1,(5,640),(5,5))

        #apple
        game_screen.fill(crimson, rect=[apple_x,apple_y,block_size,block_size])

        #snake variables
        snakehead=[]
        snakehead.append(head_x)
        snakehead.append(head_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del snakelist[0]

        for eachseg in snakelist[:-1]:
            if eachseg==snakehead:
                gameover = True

        #blit snake
        snake(block_size,snakelist)
        pygame.display.flip()

        #eating apple
        if head_x==apple_x and head_y==apple_y:
            pygame.display.update()
            apple_x = round(random.randrange(12,1080-block_size)/10.0)*10.0
            apple_y = round(random.randrange(10,635-block_size)/10.0)*10.0
            snakelength+=2

        #refreshing window
        pygame.display.flip()

        #fps
        fps.tick(fps_change)

    #quitting from pygame and python(while game_exit gets true)
    pygame.quit()
    quit()
gameLoop()
