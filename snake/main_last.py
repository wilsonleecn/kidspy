import pygame

# define variables
game_over = False

blue = (0, 0, 255)
lightblue = (50, 153, 213)
black = (0, 0, 0)
red = (255, 0, 0)

x = 200
y = 150
x_change = 0
y_change = 0

clock = pygame.time.Clock()

#init
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake Game by a genius')

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(text, colour):
    messge = font_style.render(text, True, colour)
    dis.blit(messge, [200, 100])

#background color
dis.fill(lightblue)
pygame.display.flip()

#game loop
while not game_over:
    dis.fill(lightblue)
    for event in pygame.event.get():
        #check quit
        if event.type == pygame.QUIT:
            game_over = True
        #check key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10

    #check if out of screen
    if x >= 400 or x < 0 or y >= 300 or y < 0:
        message("You lost", red)
        # game_over = True

    # get new x,y
    x += x_change
    y += y_change

    # draw snake head
    pygame.draw.rect(dis, black, [x, y, 10, 10])

    # show message
    pygame.display.update()

    clock.tick(15)

#quit
pygame.quit()
quit()