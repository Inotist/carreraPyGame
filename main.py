# Images are not of my own.
import pygame, sys

class runner:
    pass

class Game:
    runners = []
    __startLine = 0
    __finishLine = 600
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        self.runner = pygame.image.load("images/runnerA.png")
        
    def execution(self):
        x = self.__startLine
        
        gameOver = False
        while not gameOver:
            #Comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            # Refrescar / renderizar la pantalla
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 213))
            pygame.display.flip()
            
            x += 3
            if x >= self.__finishLine:
                gameOver = True
                
        pygame.quit()
        sys.exit()
                    
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.execution()