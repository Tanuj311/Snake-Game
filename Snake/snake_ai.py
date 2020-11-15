import pygame, random
pygame.init()

screen = True

def main():
    global screen
    run = True    
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    green = (0,255,0)
    score = 0
    screen_width = 624
    screen_height = 600 
    cell_size = 25
    cell_width = int(screen_width/cell_size)
    cell_height = int(screen_height / cell_size)
    win = pygame.display.set_mode((screen_width,screen_height))
    
    def space():
        keys = 'PRESS SPACE TO TURN ON AI!'
        font = pygame.font.Font(None,50)
        text = font.render(keys,True,(255,255,255))
        win.blit(text, (50,400))

    def startscreen():
        start = 'SNAKE GAME!'
        font = pygame.font.Font(None,110)
        text = font.render(start, True,(0,255,0))
        win.blit(text,(30,250))
        space()

    class snake:
        def __init__(self):
            self.length = 1
            self.pos = [screen_width - cell_width, screen_height -  cell_height]
            self.direction = UP

        def move(self):
            if self.direction == UP:
                self.pos[1] -= cell_width
            elif self.direction == RIGHT:
                self.pos[0] += cell_width
            elif self.direction == LEFT:
                self.pos[0] -= cell_height
            elif self.direction == DOWN:
                self.pos[1] += cell_height
        
        def draw(self):
            for x,y in snakelen:
                pygame.draw.rect(win,green,(int(x),int(y),cell_size,cell_size))
                pygame.draw.rect(win,(0,100,0),(int(x)+5,int(y)+5,cell_size-10,cell_size-10))

    class food:
        def __init__(self):
            self.randomx = random.randrange(0,screen_width,cell_width)
            self.randomy = random.randrange(0,screen_height,cell_height)
            self.foodpos = [self.randomx,self.randomy]

        def randompos(self):
            self.randomx = random.randrange(0,screen_width,cell_width)
            self.randomy = random.randrange(0,screen_height,cell_height)
        
        def draw(self):
            self.foodpos = [self.randomx,self.randomy]
            pygame.draw.rect(win,(255,0,0),(self.foodpos[0],self.foodpos[1],cell_size,cell_size))
        
    def redraw():
        # for x in range(0, screen_width, int(cell_width)):
        #     pygame.draw.line(win,(50,50,50), (x, 0) , (x,screen_height))
        # for y in range(0, screen_height, int(cell_height)):
        #     pygame.draw.line(win, (50,50,50), (0,y), (screen_width,y))
        apple.draw()
        man.draw()
        
    def gameover():
        over= 'GAME OVER'
        font = pygame.font.Font(None,120)
        text = font.render(over, True,(255,255,255))
        win.blit(text,(50,250)) 
        score = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            main()
    
    def showscore():
        s = f'SCORE: {score}'
        font = pygame.font.Font(None,35)
        text = font.render(s,True,(255,255,255))
        win.blit(text,(10,10))
        
    def ai():       
        if man.pos[1] <=0:
            man.direction = LEFT
            if cords[-1][0] + cell_width == cords[-2][0]:
                man.direction = DOWN
        if man.pos[0] == 0 and man.pos[1] == screen_height-cell_height:
            man.direction = RIGHT 
        if man.pos[0] == screen_width-cell_width and man.pos[1] == screen_height-cell_height:
            man.direction = UP  
        elif man.pos[0] >= cell_width:   
            if len(cords) > 2 and man.pos[1] > 0:
                if man.pos[1] == screen_height-cell_height*2 and man.direction == DOWN:
                    man.direction = LEFT
                if cords[-1][0] + cell_width == cords[-2][0]:
                    man.direction = UP   
            
    clock = pygame.time.Clock()
    man = snake()
    apple = food()
    snakelen = []
    cords = []
    over = False

    while run == True:
        if screen == True:
            startscreen()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                screen = False
        else:
            clock.tick(60)
            win.fill((0,0,0))
            key= pygame.key.get_pressed()
            if over == False:
                head = []
                head.append(man.pos[0])
                head.append(man.pos[1])
                cords.append(head)
                snakelen.append(head)
                if len(snakelen) > man.length:
                    del snakelen[0]
            if man.pos == apple.foodpos:
                apple.randompos()
                man.length+=1
                score+=1
            ai()
            man.move()
            redraw()
            showscore()
            if head in snakelen[:-1]:
                over = True
                gameover() 
                space()
            if int(snakelen[0][0]) > screen_width or int(snakelen[0][1]) > screen_height or int(snakelen[0][0]) < 0 or int(snakelen[0][1]) < 0:
                over = True
                gameover()  
                space()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

main()