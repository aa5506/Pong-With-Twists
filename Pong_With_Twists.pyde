import random, os
path = os.getcwd()

class Paddle:
    def __init__(self,x,y,v):
        self.x = x
        self.y = y
        self.v = v
        self.dir = 1
        self.vy = 0
        
        
    def update(self):
        if self.y + self.vy > 0 and self.y + self.vy < g.h - g.ln:
            self.y += self.vy
        
        
    def display(self):
        self.update()
        fill(250)
        rect(self.x,self.y,g.th,100)

            
            
class Player1(Paddle):
    def __init__(self,x,y,v):
        Paddle.__init__(self,x,y,v)
        self.keyHandler={UP:False, DOWN:False}
        
    def update(self):
        if self.y + self.vy > 0 and self.y + self.vy < g.h - g.ln:
            self.y += self.vy
        if self.keyHandler[UP]:
            self.vy = -5
            self.dir = -1
        elif self.keyHandler[DOWN]:
            self.vy = 5
            self.dir = 1
        else:
            self.vy = 0
                
            
        
class Player2(Paddle):
    def __init__(self,x,y,v):
        Paddle.__init__(self,x,y,v)
        self.keyHandler={SHIFT:False, CONTROL:False}
        
    def update(self):
        if self.y + self.vy > 0 and self.y + self.vy < g.h - g.ln:
            self.y += self.vy
        if self.keyHandler[SHIFT]:
            self.vy = -5
            self.dir = -1
        elif self.keyHandler[CONTROL]:
            self.vy = 5
            self.dir = 1
        else:
            self.vy = 0
        
        
            
            
        

        
        
        
class Game:
    def __init__(self,w,h,th,ln):
        self.w = w
        self.h = h
        self.th = th
        self.ln = ln
        self.paddle1 = Player1(0,self.h/2,0)
        self.paddle2 = Player2(self.w-self.th,self.h/2,0)
        
    def display(self):
        background(0)
        self.paddle1.display()
        self.paddle2.display()
        
    
    
    
        
        
        
g = Game(500,500,20,100)        
        
        
def setup():
    size(500,500)
    background(0)
    
def draw():
    g.display()
    
def keyPressed():
    if keyCode == UP:
        g.paddle1.keyHandler[UP] = True
    elif keyCode == DOWN:
        g.paddle1.keyHandler[DOWN] = True
    elif keyCode == SHIFT:
        g.paddle2.keyHandler[SHIFT] = True
    elif keyCode == CONTROL:
        g.paddle2.keyHandler[CONTROL] = True
        
def keyReleased():
    if keyCode == UP:
        g.paddle1.keyHandler[UP] = False
    elif keyCode == DOWN:
        g.paddle1.keyHandler[DOWN] = False
    elif keyCode == SHIFT:
        g.paddle2.keyHandler[SHIFT] = False
    elif keyCode == CONTROL:
        g.paddle2.keyHandler[CONTROL] = False
    
    
    
    
