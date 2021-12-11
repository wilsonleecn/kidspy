import pygame
from snake import Snake

# define variables
game_over = False

blue = (0, 0, 255)
lightblue = (50, 153, 213)
black = (0, 0, 0)

clock = pygame.time.Clock()
snake = Snake()

#init
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake Game by a genius')

#background color
dis.fill(lightblue)
pygame.display.flip()

#game loop
while not game_over:
    for event in pygame.event.get():
        #check quit
        if event.type == pygame.QUIT:
            game_over = True
        #check key
        if event.type == pygame.KEYDOWN:
            snake.changeDirection(event.key)

    # get new x,y
    snake.x += snake.x_change
    snake.y += snake.y_change

    # draw snake head
    dis.fill(lightblue)
    snake.draw(dis, black)

    pygame.display.update()

    clock.tick(15)

#quit
pygame.quit()
quit()