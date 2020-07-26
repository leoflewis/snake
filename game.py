import pygame
import random
import time



pygame.init()

black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)

dis_width = 800
dis_height  = 600

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('snake game by leo')

font_style = pygame.font.SysFont(None,50)
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

def user_score(score):
    value = font_style.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/3])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10.0
    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You lost! Press q to quit or c to play again.", black)
            user_score(length_of_snake)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
                
        x1 += x1_change
        y1 += y1_change
        dis.fill(red)
        
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)

        if x1 == foodx and y1 == foody:
            message("YUM!", black)
            foodx  = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody  = round(random.randrange(0, dis_height - snake_block) / 10) * 10 
            length_of_snake += 1

        user_score(length_of_snake)
        pygame.display.update()

        clock.tick(snake_speed)

    time.sleep(1)
    pygame.quit()
    quit()

game_loop()
