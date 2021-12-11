import pygame

class Snake:
    speed = 15
    blockSize = 10
    x = 200
    y = 150
    x_change = 0
    y_change = 0

    def changeDirection(self, key):
        if key == pygame.K_LEFT:
            self.x_change = -10
            self.y_change = 0
        elif key == pygame.K_RIGHT:
            self.x_change = 10
            self.y_change = 0
        elif key == pygame.K_UP:
            self.y_change = -10
            self.x_change = 0
        elif key == pygame.K_DOWN:
            self.y_change = 10
            self.x_change = 0

    def draw(self, gameboard, color):
        pygame.draw.rect(gameboard, color, [self.x, self.y, self.blockSize, self.blockSize])
