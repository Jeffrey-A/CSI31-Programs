import math
from graphics import *

def trianglearea(p1,p2,p3):
    a = p1.getX()
    b = p2.getX() 
    c = p3.getX() 
    s = a + b + c /2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return round(area,2)


def square(x):
    return x * x
def distance(p1,p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist
def main():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5),"Click on three points").draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)    
    #draw triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill('peachpuff')
    triangle.setOutline('cyan')
    triangle.draw(win)
    #perimeter
    perim = distance(p1,p2)+ distance(p2,p3) + distance(p3,p1)
    message.setText("The perimeter is:{0:0.2f}".format(perim))
    #area
    area = trianglearea(p1,p2,p3)
    message = Text(Point(5,1.5),"Click on three points").draw(win)
    message.setText("The area is:{0:0.2f}".format(area))
    
    win.getMouse()
    win.close()

main()                    
