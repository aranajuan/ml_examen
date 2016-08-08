from helpers import Helpers
from body import Body

class System:
	
    def __init__(self):
        self.sun = Body(0, 0, 0)
        self.p1 = Body(500,90,-1)
        self.p2 = Body(1000,90,5)
        self.p3 = Body(2000,90,-3)
        self.sun.setDay(0)

    def setDay(self,day):
        self.p1.setDay(day)
        self.p2.setDay(day)
        self.p3.setDay(day)
        return self.getWeather()

	# -2 sequia
	# -1 buen clima
	# >0 grado de lluvia
    def getWeather(self):
        if(Helpers.isAligned(self.p1,self.p2,self.p3)):
            if(Helpers.isAligned(self.p1,self.p2,self.sun)):
               # print 'sequia ' + str(self.p1) + str(self.p2) + str(self.p3)+ ' - ' + str(self.p1.day)
                return -2
            print 'buen clima ' + str(self.p1) + str(self.p2) + str(self.p3)
            return -1
        if(Helpers.inTriangle(self.sun,self.p1,self.p2,self.p3)):
            #print 'lluvia ' + str(self.p1) + str(self.p2) + str(self.p3)
            return Helpers.perimeter(self.p1,self.p2,self.p3)
       # print 'invalido ' + str(self.p1) + str(self.p2) + str(self.p3) + ' - ' + str(self.p1.day)
        return -3
    
    def __str__(self):
        return str(self.p1) + str(self.p2) + str(self.p3) + ' - ' + str(self.p1.day)
