#The commented commands for loading images can be uncommented to have images involved. However, that would slower down the Processing
add_library('minim')  
import random, os, time
path = os.getcwd()
player = Minim(this)

#creat Paddle class    
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
        fill(255) #fill(7,242,32) to have the green color as shown in the Arcade presentation
        rect(self.x,self.y,g.th,g.ln)

#create right paddle (Player 1), inheriting from Paddle class     
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
            
#create left paddle (Player 2), inheriting from Paddle class                    
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
            
#create Ball class        
class Ball:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 3
        self.vy = 3.5
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        #Calling functions
        self.checkBounds(self.y,self.r,self.vy)
        self.checkHit(self.x,self.r,self.y,self.vx)
        self.checkWin(self.x,self.r,self.vx)
        self.changeLength()

                
    #function to check bounds for top and bottom of screen            
    def checkBounds(self,y,r,vy):
        if self.y - self.r <= 0 or self.y + self.r >= g.h:
            x = self.vy = -self.vy
            return x
    
    #function to check collision between ball and addle    
    def checkHit(self,x,r,y,vy):
        speedlist = [0.8,0.9,1.5,1.75,2]
        if g.w - (self.x+self.r) < g.th and self.y+self.r > g.paddle1.y and self.y-self.r < g.paddle1.y + g.ln:
            if self.vx > 0:
                if self.vx < 6:
                    speed = speedlist[random.randint(0,4)] #randomly choosing values from the speedlist to vary the speed of the ball on collision with paddle1
                    self. vx = self.vx * speed
                    self.vx = -self.vx
                else:
                    self.vx = -self.vx
            g.hit.rewind()
            g.hit.play()
            
        
            
        if self.x-self.r < g.th and self.y+self.r > g.paddle2.y and self.y-self.r < g.paddle2.y + g.ln: 
            if self.vx < 0:
                if self.vx > -6:
                    speed = speedlist[random.randint(0,4)] #randomly choosing values from the speedlist to vary the speed of the ball on collision with paddle1
                    self. vx = self.vx * speed
                    self.vx = -self.vx
                else:
                    self.vx = -self.vx
            g.hit.rewind()
            g.hit.play()
    
    #function to check for win condtion i.e. if the ball crossed the screen from left or right
    def checkWin(self,x,r,vx):
        if self.x + self.r > g.w or self.x - self.r < 0:
            g.state = "gameover"
            g.music.pause()
            g.music.rewind()
            g.goSound.rewind()
            g.goSound.play()
            
    def changeLength(self):
        if g.ln > 50:
            g.ln -= 0.05

    def display(self):
        self.update()
        fill(255) #fill(7,242,32) to have the green color as shown in the Arcade presentation
        ellipse(self.x,self.y,self.r*2,self.r*2)

#create Package class (Star in game)        
class Package:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.state = "unopened"
        self.active = True
        self.star = loadImage(path+ "/images/star.png")
                
    def distance(self,ball):
        return ((self.x-ball.x)**2+(self.y-ball.y)**2)**0.5  
     
    def display(self):
        if self.state == "unopened":
            fill(255,0,0)
            image (self.star,self.x,self.y,self.r,self.r,0,0,40,40)
            #ellipse(self.x,self.y,self.r,self.r)
            if self.distance(g.ball) <= self.r + g.ball.r: 
                self.state = "opened"
                if self.active == True:
                    g.star.rewind()
                    g.star.play()                    
                    g.ball.r += 5
                    self.active = False
                       
#Creat Game class        
class Game:
    def __init__(self,w,h,th,ln,r):
        self.w = w
        self.h = h
        self.th = th
        self.ln = ln
        self.r = r
        self.pauseTime = 0
        self.cumulativePauseTime = 0
        self.timer = 0 
        self.score = 0
        self.highScore = 0
        #self.img = loadImage(path+ "/images/background.png")        
        self.state = "menu"        
    
        self.pause = False
        
        #loading sounds
        self.music = player.loadFile(path+"/sounds/music.mp3")
        self.star = player.loadFile(path+"/sounds/coin.mp3")
        self.pauseSound = player.loadFile(path+"/sounds/pause.mp3")
        self.goSound = player.loadFile(path+"/sounds/gameover.wav")
        self.hit = player.loadFile(path+"/sounds/hit.wav")
        
        #Instantiating objects from classes
        self.paddle1 = Player1(self.w-self.th,self.h/2.75,100)  
        self.paddle2 = Player2(0,self.h/2.75,100)   
        self.ball = Ball(self.w/2,self.h/2,self.r)
        
        #Creating stars with fixed positions
        self.package1 = Package(500,300,50)
        self.package2 = Package(300,300,50)
        self.package3 = Package(200,100,50)
        self.package4 = Package(550,300,50)
        self.package5 = Package(100,400,50)
        self.package6 = Package(500,300,50)
        self.package7 = Package(300,300,50)
        self.package8 = Package(200,100,50)
        self.package9 = Package(550,300,50)
        self.package10 = Package(100,400,50)
                
    
    def display(self):
        #to keep track of the time passed i.e score
        currentTime = time.time()
        elaspeTime = int(currentTime - self.timer - self.cumulativePauseTime)
        self.score = elaspeTime
        
        #opeing the highScore file to read the previous score
        x = open('highScore.txt','r')
        score = x.readline()
        self.highScore = int(score)
        x.close()
        
        #if the new score is more than the highest score, write new highest score into a file
        if self.score > self.highScore:
            y = open('highScore.txt','w')
            y.write(str(self.score))
            y.close()
    

        background(0)
        #image(self.img,0,0,640,538)
        fill(255,0,0)
        textSize(30)
        text(str(elaspeTime),self.w//2 - 10, 50)
        self.paddle1.display()
        self.paddle2.display()
        self.ball.display()
        
        #displaying star with score increments of 10 units
        self.package1.display()
        if self.score >= 10:
            self.package2.display()
        if self.score >= 20:
            self.package3.display()
        if self.score >= 30:
            self.package4.display()
        if self.score >= 40:
            self.package5.display()
        if self.score >= 50:
            self.package2.display()
        if self.score >= 60:
            self.package3.display()
        if self.score >= 70:
            self.package4.display()
        if self.score >= 80:
            self.package5.display()            
        if self.score >= 90:
            self.package4.display()
        if self.score >= 100:
            self.package5.display()    

#Intantiate object g from Game class        
g = Game(640,538,20,150,15)        
        
        
def setup():
    size(640,538)
    background(0)

    
def draw():
    
    if g.state == "menu":
        background(0)
        #title = loadImage(path+ "/images/pong.png")
        #image(title,0,0,640,538)
        
        textSize(34)
        fill (255,0,0)
        text("Pong With Twists",g.w//3 - 40 ,g.h//2 - 80) #comment this if you enable loading images
        
        #chagne color of the text when cursor moves on it
        if g.w//3 < mouseX < g.w//3 + 200 and g.h//2 < mouseY < g.h//2 + 50:
            fill(255,0,0)
        else:
            fill(255)
        text("Play Game", g.w//3 + 10, g.h//2 + 50)
        if g.w//3 < mouseX < g.w//3 + 200 and g.h//1.3 - 30 < mouseY < g.h//1.3 + 5:
            fill(255,0,0)
        else:
            fill(255)
        text("Instructions", g.w//3 + 10, g.h//1.3)
    
    #if the user wants to see instructions    
    elif g.state == "instructions":
        background(0)
        #image(g.img,0,0,640,538)
        textSize(24)
        fill(255)
        text("* Two players play as a team \n* Try to keep the ball in play as long as possible \n* Be prepared for some surprises! \n* Use left SHIFT & CTRL to move left Paddle \n* Use ARROW UP & DOWN to move right Paddle \n  (Click to go back)",g.w//12, g.h//3)

        
    elif g.state == "play":
        if not g.pause:
            background(0)
            g.display()
    
    #alerting gameover and comparing scores
    elif g.state == "gameover":
        textSize(50)
        fill (255,0,0)
        text("GAME OVER", g.w//3.5 - 10, g.h//3 +110)
        textSize(30)
        text("Your Score: " + str(g.score), g.w//3, g.h//2 +110)
        text("High Score: " + str(g.highScore), g.w//3, g.h//1.5 +110)
        

    
def mouseClicked():
    if g.state == "menu" and g.w//3 < mouseX < g.w//3 + 200 and g.h//2 < mouseY < g.h//2 + 50:
        g.state = "play"
        g.timer=time.time()
        g.music.play()
    
    elif g.state == "menu" and g.w//3 < mouseX < g.w//3 + 200 and g.h//1.3 - 30 < mouseY < g.h//1.3 + 5:
        g.state = "instructions"
        
    elif g.state == "instructions" and 0 < mouseX < g.w and 0 < mouseY < g.h:
        g.__init__(640,538,20,150,15)

        
    elif g.state == "gameover" and 0 < mouseX < g.w and 0 < mouseY < g.h:
        g.__init__(640,538,20,150,15)
        
                                
def keyPressed():
    if keyCode == UP:
        g.paddle1.keyHandler[UP] = True
    elif keyCode == DOWN:
        g.paddle1.keyHandler[DOWN] = True
    elif keyCode == SHIFT:
        g.paddle2.keyHandler[SHIFT] = True
    elif keyCode == CONTROL:
        g.paddle2.keyHandler[CONTROL] = True
    
    #game will pause if the user presses the key "P"
    elif keyCode == 80:
        if g.pause:
            g.pauseTime = time.time() - g.pauseTime
            g.cumulativePauseTime += g.pauseTime
            g.pause = False
        else:
            g.pause = True
            g.pauseTime = time.time()
            
        g.pauseSound.rewind()
        g.pauseSound.play()
        
def keyReleased():
    if keyCode == UP:
        g.paddle1.keyHandler[UP] = False
    elif keyCode == DOWN:
        g.paddle1.keyHandler[DOWN] = False
    elif keyCode == SHIFT:
        g.paddle2.keyHandler[SHIFT] = False
    elif keyCode == CONTROL:
        g.paddle2.keyHandler[CONTROL] = False
   
    
    
    
