from graphics import *
from time import sleep
def main():
    win = GraphWin("Bouncing Circle",400,400)
    win.setBackground('white')
    edg = 20
    dx = 1
    dy = 1
    circle = Circle(Point(dx,dy),5)
    circle.setFill('red')
    circle.draw(win)
    for i in range(edg):
        circle.move(dx,dy)
        dx = dx + 1
        dy = dy + 1
        sleep(0.5)    
    for i in range(edg):
        circle.move(dx,dy)
        dx = dx - 1
        dy = dy - 1 
        sleep(0.5)
        
         
    win.getMouse()
    win.close()        
            
            
        
    
    
   
main()
    