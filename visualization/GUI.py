import tkinter 
from tkinter import *

#Camera
#movement
    #camera cords is added to start&end cords
def startdrag(event):
    cc.prev = [0,0]
    cc.prev[0] = event.x_root
    cc.prev[1] = event.y_root
def drag(event):
    #event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)
    cc.campos[0] -= cc.prev[0]-event.x_root
    cc.campos[1] -= cc.prev[1]-event.y_root
    cc.prev[0] = event.x_root
    cc.prev[1] = event.y_root
    cc.redraw()
#zoom
    #multiply coords by zoom level?
def zoomIn(event):
    cc.camzoom+=0.1
    cc.campos[0] -= cc.camzoom 
    cc.campos[1] -= cc.camzoom     
    cc.redraw()
def zoomOut(event):
    cc.camzoom*=0.8
    cc.campos[0] += cc.camzoom 
    cc.campos[1] += cc.camzoom         
    cc.redraw()

class dotColor:
    def __init__(self,location,color) -> None:
        self.location = location
        self.color = color

class gridCamera:
    def __init__(self,canvas):

        canvas.bind("<B1-Motion>", drag)
        canvas.bind("<Button-1>",startdrag)
        canvas.bind("<Button-4>",zoomIn)
        canvas.bind("<Button-5>",zoomOut)

        #Camera Variables
        self.campos = [0,0]
        self.camzoom = 1
        self.C = canvas
        self.lines = []
        self.dots = []
        self.dotsColor = []

    def redraw(self):
        self.C.delete("all")
        
        for line in self.lines:
            start_x = (line[0]+self.campos[0]) * self.camzoom
            start_y = (line[1]+self.campos[1]) * self.camzoom
            end_x = (line[2]+self.campos[0]) * self.camzoom
            end_y = (line[3]+self.campos[1]) * self.camzoom
            self.C.create_line( start_x, start_y, end_x, end_y )
        
        for dot in self.dots:
            start_x = ((dot[0])+self.campos[0]) * self.camzoom
            start_y = ((dot[1])+self.campos[1]) * self.camzoom
            end_x = ((dot[0]+dot[2])+self.campos[0]) * self.camzoom
            end_y = ((dot[1]+dot[2])+self.campos[1]) * self.camzoom            
            self.C.create_oval( start_x, start_y, end_x, end_y, fill="black")

        for dot in self.dotsColor:
            start_x =   ((dot.location[0])+self.campos[0]) * self.camzoom
            start_y =   ((dot.location[1])+self.campos[1]) * self.camzoom
            end_x =     ((dot.location[0]+dot.location[2])+self.campos[0]) * self.camzoom
            end_y =     ((dot.location[1]+dot.location[2])+self.campos[1]) * self.camzoom            
            self.C.create_oval( start_x, start_y, end_x, end_y, fill=dot.color)


        self.C.place(x=0, y=0,anchor=NW)        

top = tkinter.Tk()
top.geometry("500x500")

cc = gridCamera(tkinter.Canvas(top, bg="white", width=500,height=500))
cc.dots.append([0,0,10])
cc.redraw()

def makeLine4(x1,y1,x2,y2):
    cc.lines.append([x1,y1,x2,y2])
def makeLine(lineSpec):
    cc.lines.append(lineSpec)
def makeDot(x,y,r):
    cc.dots.append([x,y,r])
def makeDot(dotSpecs):
    cc.dots.append(dotSpecs)

def makeDotColor(dotSpecs,Color):
    cc.dotsColor.append(dotColor(dotSpecs,Color))



def centerCamera(x,y):
    xCam = 250-x
    yCam = 250+y
    cc.campos = [xCam,yCam]
    cc.redraw()
def scheduleFunc(customFunc,msTime):
    top.after(msTime, customFunc)
def runGUI():
    top.mainloop()

# centerCamera(100,100)
# runGUI()