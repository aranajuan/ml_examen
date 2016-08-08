import math
from body import Body

#comparar baja precision
def feq(a,b):
    if abs(a-b)<1:
        return 1
    else:
        return 0

class Helpers:
    @staticmethod
    def distance(b1, b2):
        return math.sqrt(math.pow(b1.getX()-b2.getX(),2)+math.pow(b1.getY()-b2.getY(),2))

    @staticmethod
    def isAligned(b1, b2 , b3):
        dist12 = Helpers.distance(b1,b2)
        dist23 = Helpers.distance(b2,b3)
        dist13 = Helpers.distance(b1,b3)
        dists = sorted([dist12, dist23, dist13])
        
        #alineados perfectos
        if(feq(dists[0]+dists[1], dists[2])):
            return 1
        return 0

    @staticmethod
    def inTriangle (sun, b1,b2, b3):
        a = ((b2.getY() - b3.getY())*(sun.getX() - b3.getX()) + (b3.getX() - b2.getX())*(sun.getY() - b3.getY())) / ((b2.getY() - b3.getY())*(b1.getX() - b3.getX()) + (b3.getX() - b2.getX())*(b1.getY() - b3.getY()))
        b = ((b3.getY() - b1.getY())*(sun.getX() - b3.getX()) + (b1.getX() - b3.getX())*(sun.getY() - b3.getY())) / ((b2.getY() - b3.getY())*(b1.getX() - b3.getX()) + (b3.getX() - b2.getX())*(b1.getY() - b3.getY()))
        c = 1 - a - b
        return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1
        
    @staticmethod
    def perimeter(b1, b2 , b3):
        return Helpers.distance(b1,b2) + Helpers.distance(b2,b3) + Helpers.distance(b3,b1)
