import pygame, sys, random
from pygame.locals import *

class Runner:
    __customes = ('Barro', "Piedro", "Roco", "Stone", "Pepino")
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = self.__customes[ixCustome]
        
class Game:
    def __init__(self, background="background", display=(640,480)):
        self.__screen = pygame.display.set_mode(display)
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/{}.png".format(background))
        
        self.runner = Runner(320, 240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] -= 5
                    elif event.key == K_DOWN:
                        self.runner.position[1] += 5
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                        
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()