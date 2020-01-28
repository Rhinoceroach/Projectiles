from tkinter import *
import math

#Classes
class Player:
    def __init__(self,x,y,size,xSpeed,ySpeed,maxHp,color,canvas,direction="",player=""):
        self.x = x
        self.y = y
        self.size = size
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.maxHp = maxHp
        self.color = color
        self.c = canvas
        self.hp = maxHp
        self.direction = direction
        self.player = self.c.create_rectangle(x,y,x+size,y+size,width = size,outline=color,fill=self.color)

    def move(self,direction):
        if direction == "n":
            if not self.y <= 10:
                self.c.move(self.player, 0,-self.ySpeed)
                self.y -= self.ySpeed
        elif direction == "w":
            if not self.x <= 10:
                self.c.move(self.player, -self.xSpeed,0)
                self.x -= player.xSpeed
        elif direction == "s":
            if not self.y >= 490:
                self.c.move(self.player, 0,self.ySpeed)
                self.y += self.ySpeed
        elif direction == "e":
            if not self.x >= 490:
                self.c.move(self.player, self.xSpeed,0)
                self.x += self.xSpeed
        self.c.update()

class Projectile:
    def __init__(self,x,y,speed,size,color,canvas,active=True,time=0,xSpeed=0,ySpeed=0,projectile=""):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.speed = speed
        self.size = size
        self.color = color
        self.c = canvas
        self.time = time
        self.active = active
        if self.active:
            self.projectile = self.c.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,width = self.size,outline=self.color,fill=self.color)
        else:
            self.projectile = ""

    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
        self.c.move(self.projectile,self.xSpeed,self.ySpeed)
        self.c.update()

    def hitDetect(self,x,y):
        detect = False
        if (self.x <= x + (self.size - 1) and self.x >= x - (self.size - 1)) and (self.y <= y + (self.size - 1) and self.y >= y - (self.size - 1)):
            detect = True
        return detect

    def stop(self):
        self.xSpeed = 0
        self.ySpeed = 0
        self.active = False
        self.c.delete(self.projectile)

    def createProjectile(self,x,y):
        self.x = x
        self.y = y
        self.projectile = self.c.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,width = self.size,outline=self.color,fill=self.color)
        self.time = 0
        self.active = True

    def changeSpeed(self,xSpeed,ySpeed):
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

##class Wall:
##    def __init__(self,x,y,width,height,color,canvas,wall=""):
##        self.x = x
##        self.y = y
##        self.width = width
##        self.height = height
##        self.color = color
##        self.c = canvas
##        self.wall = self.c.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,outline=self.color,fill=color)
##
##    def hitDetect(self,x,y):
##        if (self.x <= x + (self.width - 1) and self.x >= x - (self.width - 1)) and (self.y <= y + (self.height - 1) and self.y >= y - (self.height - 1)):
##            return True
##        else:
##            return False

#Subprograms
def leftClick(event):
    global num
    if not projectiles[num].active:
        difx = event.x - player.x
        dify = event.y - player.y
        try:
            angle = math.atan(dify/difx)
        except:
            angle = 1
        projectiles[num].xSpeed = projectiles[num].speed*math.cos(angle)
        projectiles[num].ySpeed = projectiles[num].speed*math.sin(angle)
        if difx < 0:
            projectiles[num].xSpeed *= -1
            projectiles[num].ySpeed *= -1
        projectiles[num].createProjectile(player.x+projectiles[num].xSpeed+player.size/2-projectiles[num].size/2,player.y+projectiles[num].ySpeed+player.size/2-projectiles[num].size/2)
        if num != len(projectiles)-1:
            num += 1
        elif not projectiles[0].active:
            num = 0

def animate():
    player.move(player.direction)
    for x in range(len(projectiles)):
        if projectiles[x].active:
            if projectiles[x].time >= 20:
                projectiles[x].stop()
            else:
                projectiles[x].move()
                projectiles[x].time += 1
    master.after(5,animate)

def keyPressed(event):
    if event.char == "w":
        player.direction = "n"
    elif event.char == "a":
        player.direction = "w"
    elif event.char == "s":
        player.direction = "s"
    elif event.char == "d":
        player.direction = "e"

master = Tk()
master.minsize(500,500)

c = Canvas(master, width = 500, height = 500)

player = Player(200,200,10,10,10,10,"red",c)
projectiles = []
for x in range(10):
    projectiles.append(Projectile(220,220,20,5,"gray",c,False))
#wall = Wall(100,100,100,10,"black",c)
num = 0
c.bind("<Key>", keyPressed)
c.bind("<Button-1>",leftClick)
c.pack()
c.focus_set()

animate()
