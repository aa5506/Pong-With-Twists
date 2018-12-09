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
            
class Ball:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 1.5
        #self.vy = 0.2
        self.dir = 1
    def update(self):
        self.x += self.vx
        #self.y += self.vy
        self.vx = self.vx*self.dir
        right = g.w - self.x - self.r
        left = self.x - self.r
        if right <= g.th and self.y >= g.paddle1.y and self.y <= g.paddle1.y + g.ln:
            self.dir = self.dir*(-1) 
        elif left <= g.th and self.y >= g.paddle2.y and self.y <= g.paddle2.y + g.ln: 
            self.dir = self.dir*(-1) 
              


    def display(self):
        self.update()
        fill(250)
        ellipse(self.x,self.y,self.r,self.r)
            
        
        
class Game:
    def __init__(self,w,h,th,ln,r):
        self.w = w
        self.h = h
        self.th = th
        self.ln = ln
        self.r = r
        self.paddle1 = Player1(self.w-self.th,self.h/2,0)  #(0,self.h/2,0)
        self.paddle2 = Player2(0,self.h/2,0)   #(self.w-self.th,self.h/2,0)
        self.ball = Ball(self.w/2,self.h/2,self.r)
    def display(self):
        background(0)
        self.paddle1.display()
        self.paddle2.display()
        self.ball.display()
        
    
        
g = Game(500,500,20,100,30)        
        
        
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
   
    
    
    
