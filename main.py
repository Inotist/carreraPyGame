# Images are not of my own.
import pygame, sys, random, math, time

class Runner:
    def __init__(self, custome, x=0, y=0):
        self.custome = pygame.image.load("images/{}.png".format(custome))
        self.position = [x, y]
        self.name = custome
        
    def forward(self):
        self.position[0] += random.randint(1, 6)

class Game:
    __defaultNames = ("Barro", "Piedro", "Roco", "Stone", "Pepino")
    __posY = (3.609, 2.7745, 2.2535, 1.8972, 1.5841)
    __startLine = 0
    
    def __init__(self, runners="default", background="background", display=(640,480)):
        self.__screen = pygame.display.set_mode(display)
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/{}.png".format(background))
        
        self.__finishLine = math.floor(display[0] / 1.0847)
        
        self.runners = []
        self.__createRunners(runners, display)
                
    def __createRunners(self, runners, display):
        if runners is "default":
            for i in range(5):
                self.runners.append(Runner(self.__defaultNames[i], self.__startLine, math.floor(display[1]/self.__posY[i])))
        elif type(runners) is int:
            rand = [random.randint(0,4)]
            for i in range(runners):
                self.runners.append(Runner(self.__defaultNames[rand[i]], self.__startLine, math.floor(display[1]/self.__posY[i])))
                if i is 4: break
                r = random.randint(0,4)
                while r in rand: r = random.randint(0, 4)
                rand.append(r)
        elif type(runners) is tuple or type(runners) is list:
            for name in range(len(runners)):
                self.runners.append(Runner(runners[name], self.__startLine, math.floor(display[1]/self.__posY[name])))
                if name is 4: break
        
    def execution(self, tempo=0):
        gameOver = False
        self.__printGraphics()
        while True:
            if self.__checkEvents() is "quit": return
            gameOver = self.__processRace(gameOver)
            self.__printGraphics()
            # Slow down the execution to make graphic movement more observable
            time.sleep(tempo/100)
                
    def __checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
    def __processRace(self, gameOver):
        for runner in self.runners:
            runner.forward()
            if runner.position[0] >= self.__finishLine and gameOver is False:
                if __name__ == '__main__': print("{} ha ganado".format(runner.name))
                else: self.winner = runner.name
                gameOver = True
        return gameOver
            
    def __printGraphics(self):
        self.__screen.blit(self.background, (0,0))
        for runner in self.runners:
            self.__screen.blit(runner.custome, runner.position)
        pygame.display.flip()
                    
        
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        game = Game() # Default setup
#       game = Game(("BarroG", "PiedroG", "RocoG", "StoneG", "PepinoG"), "backgroundC", (1280,960)) # Test/example of different setup
    else:
        try: game = Game(int(sys.argv[1])) # Select number of random runners from the shell with default setup
        except ValueError: game = Game([runner for runner in sys.argv if runner != "main.py"]) # Select runners from the shell with default setup
        
    pygame.init()
    game.execution(1) # Use an integer to slow down execution on lower resolutions
    pygame.quit()
    
# Use game.winner to get the winner's name if executing in an external application.