import random, os
path = os.getcwd()

class Paddle:
    def __init__(self,x,y,ln):
        self.x = x
        self.y = y
        self.dir = 1
        self.vy = 0
    def update(self):
        if self.y + self.vy > 0 and self.y + self.vy < g.h - g.ln:
            self.y += self.vy
    def display(self):
        self.update()
        fill(250)
        rect(self.x,self.y,g.th,g.ln)
    
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
            
class Ball:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 3
        self.vy = 3.5
        self.xdir = 1
        self.ydir = 1
    def update(self):
    
        self.x += self.vx
        self.y += self.vy
        self.vx = self.vx*self.xdir
        self.vy = self.vy*self.ydir

        if self.y - self.r <= 0 or self.y + self.r >= g.h:
            self.ydir = self.ydir*(-1)
                
        if g.w - (self.x+self.r) <= g.th and self.y+self.r > g.paddle1.y and self.y-self.r < g.paddle1.y + g.ln:
            self.xdir = self.xdir*(-1)
        if self.x-self.r <= g.th and self.y+self.r > g.paddle2.y and self.y-self.r < g.paddle2.y + g.ln: 
            self.xdir = self.xdir*(-1)

    def display(self):
        self.update()
        fill(250)
        ellipse(self.x,self.y,self.r*2,self.r*2)
            
        
        
class Game:
    def __init__(self,w,h,th,ln,r):
        self.w = w
        self.h = h
        self.th = th
        self.ln = ln
        self.r = r
        self.paddle1 = Player1(self.w-self.th,self.h/2,100)  #(0,self.h/2,0)
        self.paddle2 = Player2(0,self.h/2,100)   #(self.w-self.th,self.h/2,0)
        self.ball = Ball(self.w/2,self.h/2,self.r)
    def display(self):
        background(0)
        self.paddle1.display()
        self.paddle2.display()
        self.ball.display()
            
    
        
g = Game(500,500,20,120,15)        
        
        
def setup():
    size(500,500)
    background(0)
    #frameRate(40)
    
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
   
    
    
    
