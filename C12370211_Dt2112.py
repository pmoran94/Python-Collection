#############################
###Author:Paul Moran
###Student No.:C12370211
###Date:11th April
#############################
'''There are 2 Constants'''
#Gavitational Force = 0.1
#Time Factor = 10
#Origin = 0.0, 0.0
'''The X&Y co-ords are adjusted based on the X & Y velocities respectively
adjusted by time.'''
#Distance from the star is calculated based on Pythagoras Theorem
'''Calculate the acceleration in both X & Y directions'''
#Acceleration = (G * Mass of Star * distance in X or Y direction)/(dist**3)



import turtle
import math

glo_scale = 150

class SUNClass:
    def __init__(self,name,radius,mass,colour):
        self.name = name;
        self.radius = radius;
        self.mass = mass;
        self.colour = colour;
        self.xCo = 0.0
        self.yCo = 0.0
        
        self.sunTur = turtle.Turtle()
        self.sunTur.shape("circle")
        self.sunTur.color(self.colour)
        self.sunTur.shapesize(self.radius/glo_scale,self.radius/glo_scale,0)

        self.sunTur.up()
        self.sunTur.goto(self.xCo,self.yCo)
        self.sunTur.down()
    def sunXCo(self):
        return self.xCo
    def sunYCo(self):
        return self.yCo
    def sunMass(self):
        return self.mass
    def sunRadius(self):
        return self.radius
    def __str__(self):
        return "Name = {},\n{} Radius = {},\n{} Mass = {},\n{} Colour = {}\n".format(self.name,self.name,self.radius,self.name,self.mass,self.name,self.colour)


class PLANETClass(SUNClass):
    def __init__(self,name,radius, mass, colour, distance, xVel,yVel):
        SUNClass.__init__(self,name,radius,mass,colour);
        self.distance = distance;
        
        self.xVel = xVel;
        self.yVel = yVel;

        self.xCo = distance * 3
        self.yCo = 0

        self.planTur = turtle.Turtle()
        self.planTur.shape("circle")
        self.planTur.color(self.colour)
        self.planTur.shapesize(self.radius/glo_scale,self.radius/glo_scale,0)

       
        #Coordinate Methods
    def pXco(self):
        return self.xCo
    def pYco(self):
        return self.yCo
    def newXCo(self,newCoX):
        self.xCo = newCoX
    def newYCo(self,newCoY):
        self.yCo = newCoY
        
        #Velocity Methods
    def curXvel(self):
        return self.xVel
    def curYvel(self):
        return self.yVel
    def newXvel(self,newXvel):
        self.xVel = newXvel
    def newYvel(self,newYvel):
        self.yVel = newYvel
        
        #Distance Methods
    def curDist(self):
        return self.distance
    def newDist(self,newD):
        self.curDist = newD
        
    def newPlanetaryPos(self):
        # fix up this code
        timeFact = .0015
        GravForce = -.0004
        
        self.distance = math.sqrt((self.pXco()**2) + (self.pYco()**2))
        
        self.xAccel = (GravForce * sunObject.sunMass() * self.pXco()) / self.distance**3
        self.xVel = (self.xVel + (self.xAccel * timeFact))
        self.xCo = (self.xCo + (self.xVel * timeFact))

        self.yAccel = (GravForce * sunObject.sunMass() * self.pYco()) / self.distance**3
        self.yVel = (self.yVel + (self.yAccel * timeFact))
        self.yCo = (self.yCo + (self.yVel * timeFact))
        self.planTur.pendown()
        
        self.planTur.goto(self.xCo,self.yCo)
    
    def __str__(self):
        return SUNClass.__str__(self) + "Distance = {},\nInitXv = {},\nInitYv = {}\n".format(self.distance, self.xVel, self.yVel)

    
class SolarSystem():
    def __init__(self,width,height):
        #self.centre = None # edit this to avoid plagiarism
        self.planetList = []
        self.screen = turtle.Screen()
        self.element = turtle.Turtle()
        self.element.hideturtle()# to hide this turtle as it does not move throughout the program
        self.screen.setworldcoordinates(-width/2, -height/2,width/2, height/2)
        self.screen.bgcolor("black")
       
    # methods to add elements to the Solar System
    def newPlanet(self,planet):
        self.planetList.append(planet)
    def myStar(self,sun):
        self.sun = sun        
    
        
'''
+++++++++++++++++++
CREATING MY OBJECTS
+++++++++++++++++++
1 SOLAR SYSTEM
1 SUN
4 PLANETS
+++++++++++++++++++
'''

# Create the solar system
mySOLSYS = SolarSystem(4,4)

#Create sun(object) from sun class
sunObject = SUNClass("myStar", 500.0, 15000.0, "yellow")
mySOLSYS.myStar(sunObject)
print(sunObject)
print("------------------")
###################################

P1Object = PLANETClass("P1",19.5,1000.0,"green",0.25,0.0,2.0 )
print(P1Object)
mySOLSYS.newPlanet(P1Object)
P1Object.planTur.up()
P1Object.planTur.setpos(P1Object.xCo,P1Object.yCo)
print(P1Object.xCo,P1Object.yCo)

print("------------------")
###################################

P2Object = PLANETClass("P2",47.5,5000.0,"blue",0.3,0.0,2.0 )
print(P2Object)
mySOLSYS.newPlanet(P2Object)
P2Object.planTur.up()
P2Object.planTur.goto(P2Object.xCo,P2Object.yCo)
print("------------------")
###################################

P3Object = PLANETClass("P3",50.0,9000.0,"red",0.5,0.0,1.63 )
print(P3Object)
mySOLSYS.newPlanet(P3Object)
P3Object.planTur.up()
P3Object.planTur.goto(P3Object.xCo,P3Object.yCo)
print("------------------")
###################################

P4Object = PLANETClass("P4",100.0,49000.0,"purple",0.7,0.0,1.0 )
print(P4Object)
mySOLSYS.newPlanet(P4Object)
P4Object.planTur.up()
P4Object.planTur.goto(P4Object.xCo,P4Object.yCo)
print("------------------")
###################################
          
var = 10000
i = 1
while i < var:
    P1Object.newPlanetaryPos()
    P2Object.newPlanetaryPos()
    P3Object.newPlanetaryPos()
    P4Object.newPlanetaryPos()
