import math

class Body:
    
    def __init__(self, sr, st, sv):
        self.sr = sr
        self.st = st
        self.sv = sv

    def setDay(self, day):
        theta = math.radians(self.st + self.sv*day)
        self.theta = theta %  ( 2 * math.pi )
        if( self.theta < 0 ):
            self.theta += ( 2 * math.pi )
        self.x = self.sr * math.cos(self.theta)
        self.y = self.sr * math.sin(self.theta) 
        self.day = day
        return self.x,self.y
    
    def getTheta(self):
        return self.theta
    
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
    
    def __str__(self):
        return '('+str(self.getX())+','+str(self.getY())+')'
